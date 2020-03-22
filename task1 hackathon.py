###hackathon Task1
select =  input("Select a GSU position")
jobdesc = input("enter a job description:")
Desctxt = open("GSU_job_descriptions.txt", "w")
Desctxt.write(jobdesc)

def save():
    text = e1.get() + "\n"+e2.get() + "\n"+e3.get() 
    with open("GSU_job_descriptions.txt", "w") as f:
        f.writelines(text)
def show():
    with open("GSU_job_descriptions.txt", "r") as f:
        f.readlines()
    e1.get(f.seek(0))
    e2.get(f.seek(1))
    e3.get(f.seek(2))
    

