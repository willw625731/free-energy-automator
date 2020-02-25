from lambda_iterator import free_energy_calc

if __name__ == '__main__':
	calc = free_energy_calc('lqd_files/top_files/PVAc1000.top', 'mol_files/top_files/Water_GMX.top',
				'lqd_files/298K/PVAc298K.gro', 'mol_files/gro_files/Water_GMX.gro', 
				0.1, 0.1, 
				'PVAc_Water_300', 'Water', 
				cpl0='none', cpl1='vdw-q', 
				mdfile_path='/ddn/data/mzkl37/mdfiles/', 
				simfile_path='/ddn/data/mzkl37/simfiles/',
	                        execute_path='/ddn/data/mzkl37/free_energy_calc/', 
				temp='300')

	calc.run_sim()
	calc = free_energy_calc('lqd_files/top_files/PVAc1000.top', 'mol_files/top_files/Ethanol_GMX.top',
				'lqd_files/298K/PVAc298K.gro', 'mol_files/gro_files/Ethanol_GMX.gro', 
				0.1, 0.1, 
				'PVAc_Ethanol_300', 'Ethanol', 
				cpl0='none', cpl1='vdw-q', 
				mdfile_path='/ddn/data/mzkl37/mdfiles/', 
				simfile_path='/ddn/data/mzkl37/simfiles/',
	                        execute_path='/ddn/data/mzkl37/free_energy_calc/', 
				temp='300')

	calc.run_sim()



# ----------------------------------------------------------------------------------------------------
# /ddn/data/mzkl37/simfiles/
#				----------------------------------------
#				lqd_files/
#						--------------------
#						298K/
#						350K/
#						500K/
#						--------------------
#						top_files/
#				----------------------------------------
#				mol_files/
#						--------------------
#						gro_files/
#						--------------------
#						top_files/
# ----------------------------------------------------------------------------------------------------

