import sys,os
import subprocess

#run_number = 0
#passive_signal_production = 0.5
#active_signal_production = 5.0
#factor_production = 0.1
#Dz=0.02;
#Rz=0.001;
#signal_thresh = 10.0
#factor_thresh = 10.0

def is_power(a,b):
  if a == 1:
    return True
  elif a%b == 0 and is_power(a/b, b) == True:
    return True
  else:
    return False

run_number = 1
for i in range(10,1001):
  if is_power(i,10):
    passive_signal_production = str(i/1000)
    for j in range(10,10001):
      if is_power(j,10) and j>i:
        active_signal_production = str(j/1000)
        for k in range(1,1001):
          if is_power(k,10):
            factor_production = str(k/1000)
            for l in range(1,10001):
              if is_power(l,10):
                Dz = str(l/10000)
                for m in range(1,1000001):
                  if is_power(m,10) and m<l:
                    Rz = str(m/100000)
                    for n in range(1000,100001):
                      if is_power(n,10):
                        signal_thresh = str(n/1000)
                        for o in range(1000,100001):
                          if is_power(o,10):
                            factor_thresh = str(o/1000)
                            for p in range(1,10001):
                              if is_power(p,10):
                                Dz_factor = str(p/10000)
                                for q in range(1,1000001):
                                  if is_power(q,10) and q<p:
                                    Rz_factor = str(q/100000)
                                    run_number += 1
                                    print "run: " + str(run_number)
                                    subprocess.Popen("python ./diffusion_3.py "+str(run_number)+" "+passive_signal_production+" "+active_signal_production+" "+factor_production+" " + Dz+" "+Rz+" "+signal_thresh+" "+factor_thresh+" "+Dz_factor+" "+Rz_factor,shell=True).wait()


