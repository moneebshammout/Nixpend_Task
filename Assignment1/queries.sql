--WORKED ON SQL LITE

--Question 1 A
SELECT 
med.Medication_id AS MedicationID,
med.Expiration_date AS MedicationExpirationDate,
CASE WHEN DATE(med.Expiration_date)<DATE('now') THEN 'Expired' ELSE 'Active' END AS MedicationStatus,
med.Doses AS MedicationDoses,
med_p.Prescription_id AS PrescriptionID,
med_p.Patient_id AS PatientID ,
count(p.Patient_id) AS patientsOnMedication
FROM 
MEDICATION AS med,
MEDICATION_PRESCRIBED AS med_p,
PATIENT AS p 
WHERE 
med.Medication_id=med_p.Medication_id and 
med_p.Patient_id=p.Patient_id  
GROUP BY MedicationId;

--Question 1 B

SELECT DISTINCT
CASE WHEN  substr(doc_p.Time, 0, 5)  <> '2022' THEN doc.Doctor_id ELSE NULL END AS DoctorID,
CASE WHEN  substr(doc_p.Time, 0, 5)  <> '2022' THEN doc.Feild ELSE NULL END AS Feild,
CASE WHEN  substr(doc_p.Time, 0, 5)  <> '2022' THEN doc.Degree ELSE NULL END AS Degree,
CASE WHEN  substr(doc_p.Time, 0, 5)  <> '2022' THEN doc.D_Worker_id ELSE NULL END AS WorkerID,
CASE WHEN  substr(doc_p.Time, 0, 5) <>'2022' THEN w.Name ELSE NULL END AS DoctorName,
CASE WHEN  substr(doc_p.Time, 0, 5) <>'2022' THEN w.Phone_Number ELSE NULL END AS DoctorPhoneNumber,
CASE WHEN  substr(doc_p.Time, 0, 5) <>'2022' THEN w.Gender ELSE NULL END AS DoctorGender,
CASE WHEN  substr(doc_p.Time, 0, 5) <>'2022' THEN w.Salary ELSE NULL END AS DoctorSalary,

dep.Department_id as DepartmentID,
dep.Workers as DepartmentWorkers,
dep.Building_location as DepartmentBuildingLocation,
doc_p.Time as TimeAttended,

p.Patient_id AS PatientID,
p.Name As PatientName,
p.Contact_Number AS PatientContactNumber,
p.Address AS PatientAddress,
p.Gender AS PatientGender,
p.Age AS PatientAge,
p.Blood_Type AS PatientBloodType,
p.Cafeteria_id AS PatientCafeteriaId ,
p.Bill_id AS PatientBillID,

FROM 
DEPARTMENT AS dep,
DOCTOR AS doc ,
DOCTOR_PATIENT AS doc_p,
PATIENT AS p,
WORKER AS w
WHERE
doc.Department_id=dep.Department_id and
doc.Doctor_id=doc_p.Doctor_id and 
doc_p.Patient_id=p.Patient_id and
w.Worker_id=doc.D_Worker_id and
p.age>12
ORDER BY
w.Name DESC,p.Name ASC;


