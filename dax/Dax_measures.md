\## Total Patients



Total Patients =

count('Healthcare Dataset'\[Name])



\--------------------------------



\## Average Billing



Admissions Count = 

count('Healthcare Dataset'\[Date of Admission])



\--------------------------------



\## Average Stay



Average Stay =

AVERAGE(Hospital\[Length of Stay])



\--------------------------------



\## Doctor Workload



Doctor Workload = 

CALCULATE(

&#x20;   COUNTROWS('Healthcare Dataset'),

&#x20;   ALLEXCEPT('Healthcare Dataset', 'Healthcare Dataset'\[Doctor]))



\--------------------------------



\## Diagnosis Count



Diagnosis Count = 

DISTINCTCOUNT('Healthcare Dataset'\[Medical Condition])



\--------------------------------



\## Total Discharges



Total Discharges = 

COUNTROWS(FILTER('Healthcare Dataset', NOT(ISBLANK('Healthcare Dataset'\[Discharge Date]))))



\--------------------------------



\## Length of Stay (Days)



Length of Stay (Days) = 

DATEDIFF('Healthcare Dataset'\[Date of Admission], 'Healthcare Dataset'\[Discharge Date], DAY)



\--------------------------------







