#!/bin/bash

MDFILE='mdmin.mdp'
GROFILE='confout.gro'
TOPFILE='topol.top'
PROCESSORS='24'
LAMBDA_STATE='0'
LV='0.0 0.2 0.4 0.6 0.8 1.0 1.0 1.0 1.0 1.0 1.0'
LQ='0.0 0.0 0.0 0.0 0.0 0.0 0.2 0.4 0.6 0.8 1.0'
CPL0='none'
CPL1='vdw-q'
MOL='molecule'
TEMP='300'

while getopts i:f:p:n:l:v:q:a:b:m:t: option; do
    case "${option}" in
	i) MDFILE=${OPTARG};;
	f) GROFILE=${OPTARG};;
	p) TOPFILE=${OPTARG};;
	n) PROCESSORS=${OPTARG};;
	l) LAMBDA_STATE=${OPTARG};;
	v) LV=${OPTARG};;
	q) LQ=${OPTARG};;
	a) CPL0=${OPTARG};;
	b) CPL1=${OPTARG};;
	m) MOL=${OPTARG};;
	t) TEMP=${OPTARG};;
    esac
done

echo 'MD file:	'$MDFILE
echo 'TOP file:	'$TOPFILE
echo 'Checks complete'

module purge
module load gromacs/plumed/ompi/gcc/2018.6
module li

sed "s/\\\$LAMBDA\\\$/${LAMBDA_STATE}/" $MDFILE > tmp.mdp
sed -i "s/\\\$LAMBDA_VDW\\\$/${LV}/" tmp.mdp
sed -i "s/\\\$LAMBDA_Q\\\$/${LQ}/" tmp.mdp
sed -i "s/\\\$COUPLE_0\\\$/${CPL0}/" tmp.mdp
sed -i "s/\\\$COUPLE_1\\\$/${CPL1}/" tmp.mdp
sed -i "s/\\\$MOLECULE\\\$/${MOL}/" tmp.mdp
sed -i "s/\\\$TEMP\\\$/${TEMP}/" tmp.mdp


gmx_mpi grompp -v -f tmp.mdp -c $GROFILE -p $TOPFILE -o topol.tpr -maxwarn 5
gmx_mpi mdrun -v -ntomp $PROCESSORS

# rm tmp.mdp



