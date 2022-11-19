import csv
maths,bio,eng,phy,che,hin=0,0,0,0,0,0
toppers_list=[]


with open("./Student_marks_list.csv", 'r') as file:
  csvreader = csv.reader(file)
  rows = list(csvreader)

  for i in range(1,len(rows)):

     if int(rows[i][1])>maths:
         maths=int(rows[i][1])

     if int(rows[i][2])>bio:
         bio=int(rows[i][2])

     if int(rows[i][3])>eng:
         eng=int(rows[i][3])

     if int(rows[i][4])>phy:
         phy=int(rows[i][4])

     if int(rows[i][5])>che:
         che=int(rows[i][5])

     if int(rows[i][6])>hin:
         hin=int(rows[i][6])

     tot=int(rows[i][1])+int(rows[i][2])+int(rows[i][3])+int(rows[i][4])+int(rows[i][5])+int(rows[i][6])
     toppers_list.append(tot)
     
    
  

  max1=max(toppers_list)
  toppers_list.remove(max1)
  max2=max(toppers_list)
  toppers_list.remove(max2)
  max3=max(toppers_list)
  
  for i in range(1,len(rows)):
      if int(rows[i][1])==maths:
          maths_top = rows[i][0]
          
      if int(rows[i][2])==bio:
          bio_top = rows[i][0]

      if int(rows[i][3])==eng:
          eng_top = rows[i][0]

      if int(rows[i][4])==phy:
         phy_top = rows[i][0]

      if int(rows[i][5])==maths:
          che_top = rows[i][0]

      if int(rows[i][6])==hin:
         hin_top = rows[i][0]

      if int(rows[i][1])+int(rows[i][2])+int(rows[i][3])+int(rows[i][4])+int(rows[i][5])+int(rows[i][6])==max1:
          top1 = rows[i][0]
      if int(rows[i][1])+int(rows[i][2])+int(rows[i][3])+int(rows[i][4])+int(rows[i][5])+int(rows[i][6])==max2:
          top2 = rows[i][0]
      if int(rows[i][1])+int(rows[i][2])+int(rows[i][3])+int(rows[i][4])+int(rows[i][5])+int(rows[i][6])==max3:
          top3 = rows[i][0]

  

  

  print("Topper in Maths is",maths_top)
  print("Topper in Biology is",bio_top)
  print("Topper in English is",eng_top)
  print("Topper in Physics is",phy_top)
  print("Topper in Chemistry is",che_top)
  print("Topper in Hindi is",hin_top)
  print("\nBest students in the class are:\n",top1,"\n",top2,"\n",top3)
  
  
    
  
