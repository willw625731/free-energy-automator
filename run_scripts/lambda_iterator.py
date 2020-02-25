import sys
import os
import free_ener_utils as fe_utils
import numpy as np


class free_energy_calc:
    def __init__(self, top_file1, top_file2, gro_file1, gro_file2, lv_step, lq_step, name, mol,
                 cpl0='vdw-q', cpl1='none', 
                 mdfile_path='/ddn/data/mzkl37/mdfiles/', 
                 simfile_path='/ddn/data/mzkl37/simfiles/',
                 execute_path='/ddn/data/mzkl37/free_energy_calc/', 
                 temp='300'):
        
        self.simfile_path = simfile_path
        self.top_file1 = self.simfile_path+top_file1
        self.top_file2 = self.simfile_path+top_file2
        self.gro_file1 = self.simfile_path+gro_file1
        self.gro_file2 = self.simfile_path+gro_file2
        self.top_final = None
        self.gro_final = None
        self.mol = None
        self.lv_count = (1.0/lv_step) + 1
        self.lq_count = (1.0/lq_step) + 1
        self.lvs = None
        self.lqs = None
        self.lvs_in = None
        self.lqs_in = None
        self.cpl0 = cpl0
        self.cpl1 = cpl1
        self.mdfile_path = mdfile_path
        self.execute_path = execute_path
        self.name = name
        self.mol = mol
        self.mdfiles = ['steep.mdp', 'l-bfgs.mdp', 'nvt.mdp', 'npt.mdp', 'production.mdp']
        self.temp = temp
        self.other_ls = None
        self.lambda_array()
 
    # Join .top files and .gro files
    def combine_files(self, top_out, gro_out, mol, count=1):
        self.top_final = top_out
        self.gro_final = gro_out
        fe_utils.top_comp(self.top_file1, self.top_file2, mol, count, top_out)
        fe_utils.comb_coords(self.gro_file1, self.gro_file2, gro_out)
    
    # Execute equil.sh script with given lambda parameters and md file
    def lambda_run(self, mdfile, lambda_idx):
        cmd = '/ddn/data/mzkl37/scripts/equil.sh -i {} -f {} -p {} -l {} -v {} -q {} -a {} -b {} -m {} -t {}'.format(
            self.mdfile_path+mdfile, 'confout.gro', self.top_final, 
            lambda_idx, self.lvs_in, self.lqs_in,
            self.cpl0, self.cpl1, self.mol, self.temp)
        os.system(cmd)
    
    # Build lambda parameter array, vdw then q
    def lambda_array(self, v0=0.0, v1=1.0, q0=0.0, q1=1.0):
        self.lvs = list(map(str, np.round(np.linspace(v0, v1, self.lv_count), 3)))
        self.lqs = list(map(str, np.round(np.linspace(q0, q1, self.lq_count), 3)))
        self.lvs = self.lvs + list(map(str, np.ones(len(self.lqs)-1)))
        self.lqs = list(map(str, np.zeros(len(self.lvs)-len(self.lqs)))) + self.lqs
        self.lvs_in = "'"+" ".join(self.lvs)+"'"
        self.lqs_in = "'"+" ".join(self.lqs)+"'"
        
    def run_sim(self):
        os.makedirs(self.execute_path+self.name)
        os.chdir(self.execute_path+self.name)
        self.combine_files(self.name+'.top', self.name+'.gro', self.mol)
        os.makedirs('xvg_out')

        # Make lambda folders
        for idx, (lv, lq) in enumerate(zip(self.lvs, self.lqs)):
            os.makedirs('lambda_lv{}_lq{}'.format(lv, lq))
            os.chdir('lambda_lv{}_lq{}'.format(lv, lq))
            os.system('cp ../{} .'.format(self.top_final))
            os.system('cp ../{} confout.gro'.format(self.gro_final))
            # Run md set for give lambdas
            for md in self.mdfiles:
                os.system('echo "MD File:\t{}\nLambdas v:\t{}\nLambdas q:\t{}"'.format(md, lv, lq))
                self.lambda_run(md, idx)
                os.system('wait')
                if not os.path.isfile('confout.gro'):
                    break
                os.system('cp confout.gro {}'.format(self.gro_final))

            os.system('cp {} {} ../'.format(self.top_final, self.gro_final))
            os.system('cp dhdl.xvg ../xvg_out/run_v{}q{}.xvg'.format(lv, lq))
            os.chdir('../')



