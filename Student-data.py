Student_details={"Student_name":["Aakash", "Aarav", "Abhishek", "Aditya", "Aisha", "Aman", "Ananya", "Anjali", "Arjun", "Ayush", "Bhavna", "Deepak",
                   "Divya", "Gaurav", "Harsh", "Ishita", "Jyoti", "Karan", "Kavya", "Khushi", "Komal", "Manish", "Meera", "Mohit", "Muskan", 
                   "Neha", "Nikhil", "Nisha", "Payal", "Pooja", "Preeti", "Priya", "Rahul", "Rakesh", "Ritika", "Riya", "Rohan", "Rohit", 
                   "Sachin", "Sakshi", "Sanjay", "Saurabh", "Shreya", "Simran", "Sneha", "Swati", "Tanvi", "Varun", "Vikram", "Yash"],
                  "Roll_No.":[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50],
                  "Fathers_name":["Rajesh Sharma", "Amit Verma", "Suresh Patel", "Manoj Gupta", "Rakesh Singh", "Vijay Kumar", "Deepak Yadav", "Anil Sharma",
                  "Mukesh Verma", "Sanjay Patel", "Pradeep Singh", "Ramesh Gupta", "Ajay Kumar", "Naresh Sharma", "Vinod Yadav", 
                 "Mahendra Patel", "Satish Verma", "Dilip Singh", "Harish Gupta", "Pankaj Sharma", "Mohan Kumar", "Jitendra Yadav", 
                 "Kailash Patel", "Subhash Verma", "Arun Singh", "Nitin Gupta", "Ravi Sharma", "Ganesh Kumar", "Shiv Yadav", "Tarun Patel", "Hemant Verma", "Dharmendra Singh",
                 "Om Prakash", "Yogesh Sharma", "Umesh Gupta","Vikram Patel", "Rajendra Verma", "Kamal Singh", "Bharat Kumar", "Sandeep Sharma", "Gaurav Mehta", "Shailendra Yadav", "Jagdish Patel",
                  "Ashok Sharma", "Rohit Saxena", "Karan Malhotra", "Ashwini Tiwari", "Naveen Choudhary", "Sachin Trivedi", "Prakash Mishra"],
                  "Grade":["D","E","E","A","B","A","C","A","C","B","D","E","A","C","C","A","C","E","A","A","B","E","C","A","B","C","E","A","A","D","C","A","A","A",
                         "A","C","D","E","C","D","A","A","C","E","A","C","E","B","A","E"]}

target=input("Enter Student Name").title()
n=len(Student_details["Student_name"])
#print(n)
l=0
r=n-1
while l<=r:
    mid=(l+r)//2
    if target==Student_details["Student_name"][mid]:
        #print(mid)
        print(f"{"Roll No."} | {"Student Name":20} | {"Father Name":20}  | {"Grade"}")
        print(f"{Student_details["Roll_No."][mid]:5}    | {Student_details["Student_name"][mid]:20} | {Student_details["Fathers_name"][mid]:20}  |  {Student_details["Grade"][mid]}" )
        break
    elif target > Student_details["Student_name"][mid]:
         l=mid+1
    else:
         r=mid-1
else:
    print("Student name is not found")
                 