

class KnowledgeBase:
    
    def Todays_Test(self):
        # Premises for the example argument
        premises = {
            'T': True,  # Today is Tuesday
            'E': None,  # I have a test in English (Unknown initially)
            'S': None,  # I have a test in Science (Unknown initially)
            'A': True   # My English Professor is absent
        }
        TesT_Logic=[]
        # Rule 1: If today is Tuesday, I have a test in English or Science
        if premises['T']:
            premises['E'] = True
            premises['S'] = True
           
        # Rule 2: If my English Professor is absent, then I will not have a test in English
        if premises['A']:
            premises['E'] = False
            
        # Rule 3: Inference
        if premises['T'] and premises['A']:
            premises['S'] = True
            
        return premises , TesT_Logic
        
    def diagnose(self):
        # Define patient symptoms
        symptoms = {
            'fever': True,
            'cough': True,
            'headache': False,
            'runny_nose': False,
            'muscle_pain': True
        }

        # Initialize possible conditions
        conditions = {
            'common_cold': False,
            'flu': False,
            'sinusitis': False,
            'pneumonia': False
        }

        # Define diagnosis rules
        # Rule 1: If a patient has fever and cough, they might have common cold or flu
        if symptoms['fever'] and symptoms['cough']:
            conditions['common_cold'] = True
            conditions['flu'] = True

        # Rule 2: If a patient has fever, cough, and headache, they might have flu or pneumonia
        if symptoms['fever'] and symptoms['cough'] and symptoms['headache']:
            conditions['flu'] = True
            conditions['pneumonia'] = True

        # Rule 3: If a patient has fever, cough, and muscle pain, they might have flu or pneumonia
        if symptoms['fever'] and symptoms['cough'] and symptoms['muscle_pain']:
            conditions['flu'] = True
            conditions['pneumonia'] = True

        # Rule 4: If a patient has fever and runny nose, they might have common cold or sinusitis
        if symptoms['fever'] and symptoms['runny_nose']:
            conditions['common_cold'] = True
            conditions['sinusitis'] = True

        return conditions

    def system_fault_diagnosis(self):
        # Define system symptoms
        symptoms = {
            'slow_performance': True,
            'crashes': True,
            'disk_full': False,
            'error_messages': True,
            'network_issues': True
        }

        # Initialize possible faults
        faults = {
            'hardware_failure': False,
            'software_bug': False,
            'disk_space_issue': False,
            'network_problem': False
        }

        # Define diagnosis rules for system faults
        # Rule 1: If the system crashes frequently and shows error messages, there might be a software bug
        if symptoms['crashes'] and symptoms['error_messages']:
            faults['software_bug'] = True

        # Rule 2: If the system is slow and crashes, there might be a hardware failure
        if symptoms['slow_performance'] and symptoms['crashes']:
            faults['hardware_failure'] = True

        # Rule 3: If the disk is full and causing slow performance, there might be a disk space issue
        if symptoms['disk_full'] and symptoms['slow_performance']:
            faults['disk_space_issue'] = True

        # Rule 4: If the system has network issues and shows error messages, there might be a network problem
        if symptoms['network_issues'] and symptoms['error_messages']:
            faults['network_problem'] = True

        return faults


# Example usage
kb = KnowledgeBase()

# Evaluate the example argument
print("Argument Evaluation:")
argument_result , Logic = kb.Todays_Test()
for i in Logic:
    print(i)
        
    
print("Therefore I have a test in Science:", argument_result['S'])
print("Therefore I have a test in English:", argument_result['E'])

# Diagnose patient based on symptoms
print("Patient Diagnosis:")
diagnosis_result = kb.diagnose()
print("Possible conditions based on symptoms:")
for condition, present in diagnosis_result.items():
    if present:
        print(condition)
print()

# Diagnose system faults based on symptoms
print("System Fault Diagnosis:")
fault_diagnosis_result = kb.system_fault_diagnosis()
print("Possible faults based on symptoms:")
for fault, present in fault_diagnosis_result.items():
    if present:
        print(fault)
