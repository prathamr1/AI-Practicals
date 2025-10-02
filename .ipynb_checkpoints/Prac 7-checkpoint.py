def medical_expert_system():
    print("Welcome to MedBot – Basic Medical Expert System")
    print("Please answer the following questions with 'yes' or 'no'\n")

    # Input from user
    fever = input("Do you have a fever? ").strip().lower()
    cough = input("Do you have a cough? ").strip().lower()
    breath = input("Are you experiencing shortness of breath? ").strip().lower()
    pain = input("Do you have chest pain? ").strip().lower()

    # Rule-based diagnosis
    print("\nDiagnosis:")
    if fever == "yes" and cough == "yes" and breath == "yes":
        print("→ You may have symptoms of a respiratory infection. Please consult a doctor immediately.")
    elif fever == "yes" and cough == "yes":
        print("→ You may have the flu or a viral infection. Rest and hydration are recommended.")
    elif pain == "yes" and breath == "yes":
        print("→ Possible cardiac issue. Seek emergency medical attention.")
    else:
        print("→ Symptoms are not conclusive. Please monitor and consult a physician if they persist.")

# Run the expert system
if __name__ == "__main__":
    medical_expert_system()
