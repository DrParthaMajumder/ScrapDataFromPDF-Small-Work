# Main Code based on  Email ID
import pandas as pd
from PyPDF2 import PdfReader
reader = PdfReader("TestData.pdf")

import re
from PyPDF2 import PdfFileReader
pdf_file_reader = PdfFileReader("TestData.pdf")


   
      
output_csv_file="DataExtratedFromPDFMain.csv"  
columns= ("company_Id,","company_details","Email","website", "phonenumber")               
for page in pdf_file_reader.pages:
    mypage=page.extractText().splitlines()
    for ii in range(len(mypage)):
        myline_split=mypage[ii].split()
        
        for jj in range (len(myline_split)):
            Email=re.findall('\w+@\w',myline_split[jj])
            if (len(Email)>0):
                myline_split1=myline_split
                print(myline_split1)
                Email=myline_split[jj]
                company_details=mypage[ii-1]  
                
                
                extract_email_form_comp_details=re.findall('\w+@\w',company_details)
                if (len(extract_email_form_comp_details)>0):
                    company_details=mypage[ii]                 
                
                extract_nasty_materials_from_comp_details=re.findall('P-Phone M-Mobile',company_details)
                if (len(extract_nasty_materials_from_comp_details)>0):
                    company_details_extracting_split=company_details.split();
                    company_details_extracting_split_strip=company_details_extracting_split[1].strip()
                    lenvalue=len(company_details_extracting_split_strip)
                    id_identified=company_details_extracting_split_strip[lenvalue-2]
                    if (id_identified.isdigit()):
                        company_details_extracting_split.remove(company_details_extracting_split[0]) 
                        company_details_extracting_split.remove(company_details_extracting_split[0]) 
                        company_details_extracting_split_joined = ' '.join(company_details_extracting_split)
                        company_details=company_details_extracting_split_joined
                        #print(company_details)
                company_details1=company_details
                company_details1_split=company_details.split()
                company_Id=company_details1_split[0]                  
                company_Id_clean=str(company_Id).replace('.','')
                if (company_Id_clean.isdigit()):
                    company_Id_final=company_Id_clean
                    company_details1_split.remove(company_details1_split[0])
                else:
                    company_Id_final=""
                    
                company_details1_final = ' '.join(company_details1_split) 
                
                
                
                # *********************************************Website***********************************
               
                
                website=[]                               
                for kk in range(len(myline_split1)):
                    website_double_check=re.findall('www.',myline_split1[kk])
                    if (len(website_double_check)>0):
                        website=myline_split1[kk] 
                    
                                     
                print("website:",website)        
               
                              
                
                # ***********************Phone Number **************************************************
                phonenumber=[] 
                myline_split1_string=' '.join(myline_split1)
                myline_split1_string_cleaned=re.sub('-','', str(myline_split1_string))
                mystrcleaned_split=myline_split1_string_cleaned.split()
                for kk in range(len(mystrcleaned_split)):
                    if (mystrcleaned_split[kk].isdigit()):
                        phonenumber=mystrcleaned_split[kk]
                print("phonenumber:",phonenumber)
                
                columndata=(company_Id_final,company_details1_final, Email, website, phonenumber)  
                df=pd.DataFrame(columndata,index=columns).T
                with open(output_csv_file, 'a') as f:
                    (df).to_csv(f,header=False)
                    
                
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        