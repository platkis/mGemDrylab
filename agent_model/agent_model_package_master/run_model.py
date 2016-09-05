import sys,os
import subprocess
import datetime

#run_number = 0
#passive_signal_production = 0.5
#active_signal_production = 5.0
#factor_production = 0.1
#Dz=0.02;
#Rz=0.001;
#signal_thresh = 10.0
#factor_thresh = 10.0

start = int(input("start: "))
end = int(input("end: "))
print("Thank you! (^-^)")


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
    passive_signal_production = str(float(i)/1000.0)
    for j in range(10,10001):
      if is_power(j,10) and j>i:
        active_signal_production = str(float(j)/1000.0)
        for k in range(1,1001):
          if is_power(k,10):
            factor_production = str(float(k)/1000.0)
            for l in range(1,10001):
              if is_power(l,10):
                Dz = str(float(l)/10000.0)
                for m in range(1,10001):
                  if is_power(m,10) and m<l:
                    Rz = str(float(m)/100000.0)
                    for n in range(1000,1000001):
                      if is_power(n,10):
                        signal_thresh = str(float(n)/10000.0)
                        for o in range(1000,1000001):
                          if is_power(o,10):
                            factor_thresh = str(float(o)/10000.0)
                            for p in range(1,10001):
                              if is_power(p,10):
                                Dz_factor = str(float(p)/10000.0)
                                for q in range(1,10001):
                                  if is_power(q,10) and q<p:
                                    Rz_factor = str(float(q)/100000.0)
                                    run_number += 1
                                    if run_number >= start and run_number <= end:
                                      print("run: " + str(run_number))
                                      start_time = datetime.datetime.now()
                                      subprocess.Popen("python ./agent_model.py "+str(run_number)+" "+passive_signal_production+" "+active_signal_production+" "+factor_production+" " + Dz+" "+Rz+" "+signal_thresh+" "+factor_thresh+" "+Dz_factor+" "+Rz_factor,shell=True).wait()
                                      end_time = datetime.datetime.now()
                                      print("run time: " + str(end_time - start_time))

