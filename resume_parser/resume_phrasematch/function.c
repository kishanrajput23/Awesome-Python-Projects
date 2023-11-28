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
int search(char pattern[10],char filecontent[30])//function to check if given pattern is present in the file passed,returns non zero if found.
{

        if(strstr(filecontent,pattern)!=NULL)//at this step,if the pattern is found,the char array pattern points to the location at which the pattern was found in the contents of the file,hence we need to reassign it to the required pattern at every iteration
        {
            return 1;
        }
        else
        {
            return 0;
        }
}

int operator_check(char op[4])
{
    if((op[0]=='O'&&op[1]=='R')||(op[0]=='o'&&op[1]=='r'))
    {
        return 1;
    }
    else if((op[0]=='A'&&op[1]=='N'&&op[2]=='D')||(op[0]=='a'&&op[1]=='n'&&op[2]=='d'))
    {
        return 2;
    }
    else {
        return 0;
    }
}



void files_with_pattern(int counter,char *files[20])
{
    int i;
    printf("---------------------------------------------------\n");
    printf("Number of files containing the given pattern= %d\n",counter);
    printf("---------------------------------------------------\n");
    printf("list of the location of files containing given pattern:\n");
    for(i=0;i<counter;i++)
     {
         printf("file %d = %s\n",i+1,files[i]);
     }
    printf("---------------------------------------------------\n");

}
