import pandas as pd
import numpy as np

# Load the input files
col = ['ID', 'Xmin', 'Xmax', 'Ymin', 'Ymax']

#milestone-2
care_areas = pd.read_csv(r"C:\Users\skava\Downloads\Dataset-1\4th\CareAreas.csv", names=col, header=None)
metadata = pd.read_csv(r"c:\Users\skava\Downloads\Dataset-1\4th\metadata.csv")



# Set the size of main field and sub field

main_field_size = metadata.loc[0, 'Main Field']
sub_field_size = metadata.loc[0, 'Sub Field size']
print(main_field_size,sub_field_size)



main_field = []
sub_field=[]
main_field_index=-1
for care_area in care_areas.index:
    main_field_coord=[]
    main_field_index+=1
    main_field_coord.append(main_field_index)
    print(care_areas['Xmin'][care_area])
    X1 = care_areas['Xmin'][care_area]
    Y1 = care_areas['Ymin'][care_area]
    X2 = care_areas['Xmax'][care_area]
    Y2 = care_areas['Ymax'][care_area]
    
    main_field_Xmin = ((X1+X2)/2) - (main_field_size/2)       # generating coordinates of main field.
    main_field_Xmax = ((X1+X2)/2) + (main_field_size/2)
    main_field_Ymin = ((Y1+Y2)/2) - (main_field_size/2)
    main_field_Ymax = ((Y1+Y2)/2) + (main_field_size/2)
    
    
     
    main_field_coord.append(main_field_Xmin)
    main_field_coord.append(main_field_Xmax)
    main_field_coord.append(main_field_Ymin)
    main_field_coord.append(main_field_Ymax)
    
    main_field.append(main_field_coord)     # appending current coordinates of main field to main feild list
    print("Main field coordinates : ",main_field_coord," index = ",main_field_index) 
    
  
 

  
    for x in np.arange((X1), (X2), (sub_field_size)):
        for y in np.arange((Y1), (Y2), (sub_field_size)):
            sub_field_Xmin = x
            sub_field_Xmax = x + sub_field_size
            sub_field_Ymin = y
            sub_field_Ymax = y + sub_field_size
            # Append sub field coordinates to the list
            sub_field_coord = [sub_field_Xmin, sub_field_Xmax, sub_field_Ymin, sub_field_Ymax, main_field_index] 
            sub_field.append(sub_field_coord)
    


               
            
sub_fd_df = pd.DataFrame(sub_field) 
sub_fd_df.to_csv('subfield-4.csv',header=False)               
main_field_df =  pd.DataFrame(main_field)
main_field_df.to_csv('mainfield-4.csv',index=False,header=False)              

  