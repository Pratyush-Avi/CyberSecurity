#include<stdio.h>
#include<string.h>
 
int main(){
    char text[100];
    printf("PRATYUSH AVI A203 \n");
   	printf("Enter a text : ");
	gets(text);
    int cipher;
    printf("Enter key: ");
	scanf("%d", &cipher);

    int textlen = strlen(text);
    int i, j, k = -1, r = 0, co = 0;
    char railmat[cipher][textlen];
 
    for(i = 0; i < cipher; ++i)
        for(j = 0; j < textlen; ++j)
            railmat[i][j] = '\n';
 
    for(i = 0; i < textlen; ++i){
        railmat[r][co++] = text[i];
 
        if(r == 0 || r == cipher-1)
            k= k * (-1);
 
        r = r + k;
    }
 
    printf("\nRail Fence Cipher Text: ");
 
    for(i = 0; i < cipher; ++i)
        for(j = 0; j < textlen; ++j)
            if(railmat[i][j] != '\n')
                printf("%c", railmat[i][j]);

 
return 0;
 
}
