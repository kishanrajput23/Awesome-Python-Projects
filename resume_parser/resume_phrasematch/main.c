/*
Name: SUDHANVA RAJESH
SRN: PES1UG19CS512
SEC: Q
ROLL NUMBER: 58
SUBJECT:PSWC
SUBJECT CODE:UE19CS151
TEACHER IN CHARGE: SUPREETHA S

Some requirements for the program to work:
1.In the command line arguments passed,the complete location of the files in which the pattern has to be searched (for example C:\Users\sudhanva\Desktop\pswc_project\test1.txt),must be entered properly,without any mistake,if the file is present in a different folder, if the file is located in the same folder as the program, only mentioning the name of the file i.e. file1.txt for example is sufficient
2.A maximum of 20 files entered can contain required pattern,this can be increased,but care must be taken to increase the size of the files array declared in the main function.
3.The pattern can be 10 characters long,this can be increased by increasing the size of the pattern array,and the temp_pattern array declared in the main function.
4.In the files passed,the last character of the file must be followed by a tab space,so that the program can recognize the end of the file, multi line files are accepted.
5.The files passed,must not have any tab spaces,at any part of the file other than the end of the file.This is the only problem with the program i was not able to overcome.
6.First command line argument=first pattern, Second command line argument=Second pattern, Third command line argument=conditional operator, Fourth command line argument onwards=files
*/

#include"header.h"
#include<stdio.h>
#include<string.h>
int main(int argc,char *argv[])
{
   int i=1,k=0,counter=0;
   char pattern1[10],pattern2[10],op[4],*files[20];
   FILE *f;
   strcpy(pattern1,argv[1]);
   strcpy(pattern2,argv[2]);
   strcpy(op,argv[3]);
   printf("---------------------------------------------------\n");
   printf("Files locations:\n");
   for(i=4;i<argc;i++)
   {
       printf("%s\n",argv[i]);
   }
   for(i=4;i<argc;i++)
   {
     k=0;
     char filecontent[30]="";
     printf("---------------------------------------------------\n");
     printf("Current file being searched:\n%s\n",argv[i]);
     f=fopen(argv[i],"r");
     char c;
     while(1)
     {
            filecontent[k]=fgetc(f);
            k++;
            if(feof(f))
                break;
     }
     /*
     printf("- - - - - - - - - - - - - - - - - - - - - - - - - -\n");
     printf("File content\n%s\n",filecontent);
     printf("- - - - - - - - - - - - - - - - - - - - - - - - - -\n");  //remove this set of comments if the file that is being searched needs to be shown at each iteration,while making the program i used this set of code for better clarity as to which file is opened etc.
     printf("Pattern1\n%s\n",pattern1);
     printf("- - - - - - - - - - - - - - - - - - - - - - - - - -\n");  //remove this set of comments if the file that is being searched needs to be shown at each iteration,while making the program i used this set of code for better clarity as to which file is opened etc.
     printf("Pattern2\n%s\n",pattern2);
     printf("- - - - - - - - - - - - - - - - - - - - - - - - - -\n");
     */
     fclose(f);
     switch(operator_check(op))
     {
     case 1:
         {
           if((search(pattern1,filecontent)!= 0)||(search(pattern2,filecontent)!= 0))
           {
               strcpy(pattern1,argv[1]);
               strcpy(pattern2,argv[2]);//we are doing this step because after performing strstr(filecontent,pattern) in the search function,the array pattern points to the location at which the pattern was found in the file's content,and hence we need to reassign it at every iteration
               files[counter]=argv[i];
               printf("status: found\n");
               counter++;
           }
           else
           printf("status: not found\n");

           break;
         }
     case 2:
        {
           if((search(pattern1,filecontent)!= 0)&&(search(pattern2,filecontent)!= 0))
           {
               strcpy(pattern1,argv[1]);
               strcpy(pattern2,argv[2]);//we are doing this step because after performing strstr(filecontent,pattern) in the search function,the array pattern points to the location at which the pattern was found in the file's content,and hence we need to reassign it at every iteration
               files[counter]=argv[i];
               printf("status: found\n");
               counter++;
           }
           else
           printf("status: not found\n");
           break;
        }
     }

   }
   files_with_pattern(counter,files);
   return 0;
}
