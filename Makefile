# This make file is set up to work with each node being configured with the
# hostname 'node-[n]'. SSH keys must be installed.
check-cluster:
	mpiexec -n 4 --host node-1,node-2,node-3,node-4 hostname

test: fournode-fourcore fournode-onecore local-fourcore local-onecore

testVal =  500000 1000000 1500000 2000000 2500000 3000000 3500000 4000000 4500000 5000000 5500000 6000000 6500000 7000000 7500000 8000000 8500000 9000000 9500000 10000000

fournode-fourcore:
	@printf "\nfournode-fourcore\n" ;
	@- $(foreach X,$(testVal), \
		mpiexec -n 4 --host node-1,node-2,node-3,node-4 python3 ~/mpiTests/primeMP.py $X -s 4;\
	)
	
fournode-onecore:
	@printf "\nfournode-onecore\n" ;
	@- $(foreach X,$(testVal), \
		mpiexec -n 4 --host node-1,node-2,node-3,node-4 python3 ~/mpiTests/primeMP.py $X -s 1;\
	)

onenode-fourcore:
	@printf "\nonenode-fourcore\n" ;
	@- $(foreach X,$(testVal), \
		mpiexec -n 1 --host node-1 ~/mpiTests/primeMP.py $X -s 4;\
	)

local-eightcore:
	@printf "\nlocal-eightcore\n" ;
	@- $(foreach X,$(testVal), \
		python3  ./primeMPLocal.py $X -s 8;\
	)

local-fourcore:
	@printf "\nlocal-fourcore\n" ;
	@- $(foreach X,$(testVal), \
		python3  ./primeMPLocal.py $X -s 4;\
	)

local-onecore:
	@printf "\nlocal-onecore\n" ;
	@- $(foreach X,$(testVal), \
		python3  ./primeMPLocal.py $X -s 1;\
	)


sync:
	rsync -vha --exclude=".git" ./ node-1:~/mpiTests/
	rsync -vha --exclude=".git" ./ node-2:~/mpiTests/
	rsync -vha --exclude=".git" ./ node-3:~/mpiTests/
	rsync -vha --exclude=".git" ./ node-4:~/mpiTests/