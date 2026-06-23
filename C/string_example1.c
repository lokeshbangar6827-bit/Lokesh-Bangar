#include<stdio.h>
int main(){
    char name[]="ram";
    printf("%s\n",name);
    printf("%c\n",name[1]);
    
    name[0]='P';
    name[1]='a';
    printf("%s\n",name);
    return 0;
}