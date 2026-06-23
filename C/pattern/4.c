# include <stdio.h>
int main(){
    for(int i=1;i<=4;i++){
       for(int j=3;j>=i;j--){
            printf(" ");
        }
        for(int k=1;k<=i;k++){
            printf("* ");
       }
       printf("\n");
    }
      for(int i=3;i>=1;i--){
       for(int j=3;j>=i;j--){
            printf(" ");
        }
        for(int k=1;k<=i;k++){
            printf("* ");
       }
       printf("\n");
    }
    
    
    return 0;
}