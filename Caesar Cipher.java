#include<stdio.h>
 
int main()
{
	char text[100], re;
	int i, k,temp;
	printf("PRATYUSH AVI A203 \n");
	printf("Enter a text : ");
	gets(text);
	printf("Choose the option (1 or 2):");
	scanf("%d",&temp);
	
	if(temp == 1)
	{
	printf("Enter key: ");
	scanf("%d", &k);
	
	for(i=0; text[i]!='\0'; ++i)
	{
		re=text[i];
		
		if(re>=97 && re<=122)
		{
			re=re+k;
			
			if(re>122)
			{
				re=re - 122 + 97 - 1;
			}
			
			text[i]=re;
		}
		else if(re>=65 && re<=90)
		{
			re=re+k;
			
			if(re>90)
			{
				re=re - 90 + 65 -1;
			}
			
			text[i]=re;
		}
	}
	printf("Encryption:%s",text);
	return 0;
	}
	else if(temp==2)
	{
	printf("Enter key: ");
	scanf("%d", &k);
	
	for(i=0; text[i]!='\0'; ++i){
		re=text[i];
		
		if(re>=97 && re<=122){
			re=re-k;
			
			if(re<97){
				re= re + 122 - 97 +1;
			}
			
			text[i]=re;
		}
		else if(re>=65&&re<=90){
			re=re-k;
			
			if(re<65){
				re=re + 90 - 65 +1;
			}
			
			text[i]=re;
		}
	}
	
	printf("Decrypted text: %s", text);
	
	return 0;
    } 

	else
	{
	    printf("Please choose the available option");
	}
    	
}
