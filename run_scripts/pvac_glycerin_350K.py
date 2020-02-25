from lambda_iterator import free_energy_calc

if __name__ == '__main__':
	calc = free_energy_calc('lqd_files/top_files/PVAc1000.top', 'mol_files/top_files/Glycerin_GMX.top',
				'lqd_files/350K/PVAc350K.gro', 'mol_files/gro_files/Glycerin_GMX.gro', 
				0.1, 0.1, 
				'PVAc_Glycerin_350', 'Glycerin', 
				cpl0='none', cpl1='vdw-q', 
				mdfile_path='/ddn/data/mzkl37/mdfiles/', 
				simfile_path='/ddn/data/mzkl37/simfiles/',
	                        execute_path='/ddn/data/mzkl37/free_energy_calc/', 
				temp='350')

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

