using LinearAlgebra
d = 0.0001;
Au = [0 1; 1 -d];
eAu = eigen(Au);
Ad = [0 1; -1 -d];
eAd = eigen(Ad);

println(eAu);
println(eAd);
