#include<stdio.h>
#include<stdlib.h>
#include<time.h>
main()
{  
int magic1,magic2 , s=1 ,x,t ,count=0;
 
char a;
 
     srand(time(NULL));

      
loop1:
	
 magic1=rand()%50+1;
		magic2= rand()%30+1;
		if(magic1<magic2)
		{
			magic1=magic2;
			magic2=magic1;
		}
		t=rand()%2+0;
		 
		if(t==0){a='+',s=magic1+magic2;}
		if(t==1){a='-',s=magic1-magic2;}
		 
	 printf("%d%c%d\n",magic1,a,magic2);
	 printf("�����: \n",x);
	scanf("%d",&x);
	if(s==x)   
	{
		printf("��ȷ����˶�����\n ");
		goto  loop1;
		}
	else
	{
		printf("����!���´���\n");
	}
		do{
			printf("�����: \n",x);
	scanf("%d",&x);
	count++;
	if(s==x)
	{printf("��ȷ!��������������⣡\n");
	goto loop1;
	}
	 
		}while(count!=4);
		printf("��������������5���ˣ����������ˣ��ú�����ɣ�");
     
	
}