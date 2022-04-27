# importing module
from pandas import *
from statistics import mean
import numpy as np


def compute_average(list):
    sum = 0
    count = 0
    for i in range(len(list)):
        if list[i]!='' and list[i]!=' ':
            sum = sum + float(list[i])
            count = count + 1
    
    if count!= 0:
        return sum/count
    else:
        return 0


def read_inputs():


    # Data Reading
    
    # reading CSV file
    data = read_csv("data_input/OppScrData.csv",keep_default_na=False,low_memory=False)

    # ======================= Clinic Data =====================================
    Clinic_Data = []
    Clinic_Data.append(data['Record ID'].tolist())                                          # Col A
    Clinic_Data.append(data['Visit ID'].tolist())                                           # Col B
    Clinic_Data.append(data['PT ID'].tolist())                                              # Col C
    Clinic_Data.append(data['Clinical F/U interval  [d from CT]'].tolist())                 # Col D
    Clinic_Data.append(data['BMI'].tolist())                                                # Col E
    Clinic_Data.append(data['BMI >30'].tolist())                                            # Col F
    Clinic_Data.append(data['Sex'].tolist())                                                # Col G
    Clinic_Data.append(data['Age at CT'].tolist())                                          # Col H
    Clinic_Data.append(data['Tobacco'].tolist())                                            # Col I
    Clinic_Data.append(data['Alcohol abuse'].tolist())                                      # Col J
    Clinic_Data.append(data['FRS 10-year risk (%)'].tolist())                               # Col K
    Clinic_Data.append(data['FRAX 10y Fx Prob (Orange-w/ DXA)'].tolist())                   # Col L
    Clinic_Data.append(data['FRAX 10y Hip Fx Prob (Orange-w/ DXA)'].tolist())               # Col M
    Clinic_Data.append(data['Met Sx'].tolist())                                             # Col N

    # ======================= Outcome Data =====================================
    Outcome_Data = []
    Outcome_Data.append(data['DEATH [d from CT]'].tolist())                                 # Col P
    Outcome_Data.append(data['CVD DX'].tolist())                                            # Col Q
    Outcome_Data.append(data['CVD DX Date [d from CT]'].tolist())                           # Col R
    Outcome_Data.append(data['Heart failure DX'].tolist())                                  # Col S
    Outcome_Data.append(data['Heart failure DX Date [d from CT]'].tolist())                 # Col T
    Outcome_Data.append(data['MI DX'].tolist())                                             # Col U
    Outcome_Data.append(data['MI DX Date [d from CT]'].tolist())                            # Col V
    Outcome_Data.append(data['Type 2 Diabetes DX'].tolist())                                # Col W
    Outcome_Data.append(data['Type 2 Diabetes DX Date [d from CT]'].tolist())               # Col X
    Outcome_Data.append(data['Femoral neck fracture DX'].tolist())                          # Col Y
    Outcome_Data.append(data['Femoral neck fracture DX Date [d from CT]'].tolist())         # Col Z
    Outcome_Data.append(data['Unspec femoral fracture DX'].tolist())                        # Col AA
    Outcome_Data.append(data['Unspec femoral fracture DX Date [d from CT]'].tolist())       # Col AB
    Outcome_Data.append(data['Forearm fracture DX'].tolist())                               # Col AC
    Outcome_Data.append(data['Forearm fracture DX Date [d from CT]'].tolist())              # Col AD
    Outcome_Data.append(data['Humerus fracture DX'].tolist())                               # Col AE
    Outcome_Data.append(data['Humerus fracture DX Date [d from CT]'].tolist())              # Col AF
    Outcome_Data.append(data['Pathologic fracture DX'].tolist())                            # Col AG
    Outcome_Data.append(data['Pathologic fracture DX Date [d from CT]'].tolist())           # Col AH
    Outcome_Data.append(data['Alzheimers DX'].tolist())                                     # Col AI
    Outcome_Data.append(data['Alzheimers DX Date [d from CT]'].tolist())                    # Col AJ
    Outcome_Data.append(data['Primary Cancer Site'].tolist())                               # Col AK
    Outcome_Data.append(data['Primary Cancer Dx [d from CT]'].tolist())                      # Col AL
    Outcome_Data.append(data['Primary Cancer Site 2'].tolist())                             # Col AM
    Outcome_Data.append(data['Primary Cancer Site 2 Dx [d from CT]'].tolist())              # Col AN

    # ======================= CT Data =====================================
    CT_Data = []
    CT_Data.append(data['L1_HU_BMD'].tolist())                                              # Col AP
    CT_Data.append(data['TAT Area (cm2)'].tolist())                                         # Col AQ
    CT_Data.append(data['Total Body                Area EA (cm2)'].tolist())                # Col AR
    CT_Data.append(data['VAT Area (cm2)'].tolist())                                         # Col AS
    CT_Data.append(data['SAT Area (cm2)'].tolist())                                         # Col AT
    CT_Data.append(data['VAT/SAT     Ratio'].tolist())                                      # Col AU
    CT_Data.append(data['Muscle HU'].tolist())                                              # Col AV
    CT_Data.append(data[' Muscle Area (cm2)'].tolist())                                     # Col AW
    CT_Data.append(data['L3 SMI (cm2/m2)'].tolist())                                        # Col AX
    CT_Data.append(data['AoCa        Agatston'].tolist())                                   # Col AY
    CT_Data.append(data['Liver HU    (Median)'].tolist())                                   # Col AZ

    # Data Preprocessing
    # ======================= Clinic Data =====================================
    # BMI - If BMI is unknown, we assign an average BMI value
    average_BMI = mean([float(l) for l in Clinic_Data[4] if l!=''])
    for i in range(len(Clinic_Data[4])):
        if Clinic_Data[4][i] == '' or Clinic_Data[4][i] == ' ':
            Clinic_Data[4][i] = average_BMI

    # BMI >30 - 0 for N, 1 for Y
    for i in range(len(Clinic_Data[5])):
        if Clinic_Data[5][i] == 'N':
            Clinic_Data[5][i] = 0
        elif Clinic_Data[5][i] == 'Y':
            Clinic_Data[5][i] = 1
        else:
            if float(Clinic_Data[4][i]) > 30:
                Clinic_Data[5][i] = 1
            else:
                Clinic_Data[5][i] = 0


    # Sex - 0 for female, 1 for male
    for i in range(len(Clinic_Data[6])):
        if Clinic_Data[6][i] == 'Female':
            Clinic_Data[6][i] = 0
        elif Clinic_Data[6][i] == 'Male':
            Clinic_Data[6][i] = 1

    # Tobacco - -1 for 'No', 1 for 'Yes', 0 for unknown
    for i in range(len(Clinic_Data[8])):
        if Clinic_Data[8][i] == 'Yes':
            Clinic_Data[8][i] = 1
        elif Clinic_Data[8][i] == 'No':
            Clinic_Data[8][i] = -1
        else:
            Clinic_Data[8][i] = 0

    # Alcohol Abuse
    # We categorize alcohol abuse into several levels:
    # 5 - Acute alcoholic intoxicational alcoholism
    # 4 - Alcohol abuse
    # 3 - Alcohol dependence
    # 2 - Alcohol use
    # 1 - Other and unspecified
    for i in range(len(Clinic_Data[9])):
        if Clinic_Data[9][i] == 'Acutealcoholicintoxicationinalcoholism,continuous' or Clinic_Data[9][i] == 'Acutealcoholicintoxicationinalcoholism,unspecified':
            Clinic_Data[9][i] = 5
        elif Clinic_Data[9][i] == 'Alcoholabuse,uncomplicated' or Clinic_Data[9][i] == 'Alcoholabuse,inremission' or Clinic_Data[9][i] == 'Alcoholabusewithintoxication,unspecified' or Clinic_Data[9][i] == 'Alcoholabusewithotheralcohol-induceddisorder':
            Clinic_Data[9][i] = 4
        elif Clinic_Data[9][i] == 'Alcoholdependence,uncomplicated' or Clinic_Data[9][i] == 'Alcoholdependence,inremission' or Clinic_Data[9][i] == 'Alcoholdependencewithwithdrawal,unspecified' or Clinic_Data[9][i] == 'Alcoholdependencewithintoxication,unspecified' or Clinic_Data[9][i]=='Alcoholdependencewithwithdrawaldelirium':
            Clinic_Data[9][i] = 3
        elif Clinic_Data[9][i] == 'Alcoholuse,unspecifiedwithintoxication,uncomplicated' or Clinic_Data[9][i] == 'Alcoholuse,unspecifiedwithunspecifiedalcohol-induceddisorder' or Clinic_Data[9][i] == 'Alcoholuse,unspecifiedwithalcohol-inducedsleepdisorder':
            Clinic_Data[9][i] = 2
        elif Clinic_Data[9][i] == 'Otherandunspecifiedalcoholdependence,unspecifieddrinkingbehavior' or Clinic_Data[9][i] == 'Otherandunspecifiedalcoholdependence,continuousdrinkingbehavior' or Clinic_Data[9][i]=='Otherandunspecifiedalcoholdependence,inremission' or Clinic_Data[9][i]=='Otherandunspecifiedalcoholdependence,episodicdrinkingbehavior':
            Clinic_Data[9][i] = 1
        elif Clinic_Data[9][i] == '' or Clinic_Data[9][i] == ' ':
            Clinic_Data[9][i] = 0

    # FRS 10-year Risk
    # TODO
    # we consider <1 to be 0.005, >30 to be 0.4, if unknown then we give 0
    for i in range(len(Clinic_Data[10])):
        if Clinic_Data[10][i] == '<1%':
            Clinic_Data[10][i] = 0.005
        elif Clinic_Data[10][i] == '>30%':
            Clinic_Data[10][i] = 0.4
        elif Clinic_Data[10][i] == 'X':
            Clinic_Data[10][i] = 0
        else:
            Clinic_Data[10][i] = float(Clinic_Data[10][i].strip('%'))/100

    # FRAX 10y Fx Prob (Orange-w/ DXA)
    # FRAX 10y Hip Fx Prob (Orange-w/ DXA)
    # convert '_' to 0 for both columns
    for i in range(len(Clinic_Data[11])):
        if Clinic_Data[11][i] == '_':
            Clinic_Data[11][i] = 0
        else:
            Clinic_Data[11][i] = float(Clinic_Data[11][i])
        
    for i in range(len(Clinic_Data[12])):
        if Clinic_Data[12][i] == '_':
            Clinic_Data[12][i] = 0
        else:
            Clinic_Data[12][i] = float(Clinic_Data[12][i])

    # Met Sx
    # set -1 if 'N', set 1 if 'Y', set 0 if unknown
    for i in range(len(Clinic_Data[13])):
        if Clinic_Data[13][i] == '' or Clinic_Data[13][i] == ' ':
            Clinic_Data[13][i] = 0
        elif Clinic_Data[13][i] == 'N':
            Clinic_Data[13][i] = -1
        elif Clinic_Data[13][i] == 'Y':
            Clinic_Data[13][i] = 1




    # Data Preprocessing
    # ======================= CT Data =====================================
    # fill in unknowns with mean value of all known fields
    for i in range(len(CT_Data)):
        average = compute_average(CT_Data[i])
        for j in range(len(CT_Data[i])):
            if CT_Data[i][j] == '' or CT_Data[i][j] == ' ':
                CT_Data[i][j] = average



    # Data Preprocessing
    # ======================= Clinical Data =====================================
    for i in range(len(Outcome_Data)):
        for j in range(len(Outcome_Data[i])):
            if Outcome_Data[i][j] == '' or Outcome_Data[i][j] == ' ':
                Outcome_Data[i][j] = 0
            else:
                Outcome_Data[i][j] = 1

    return Clinic_Data, Outcome_Data, CT_Data
