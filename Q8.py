int main(void){
    char str[500];
    int i,j,t;
    printf("Input a string...\nstr=");
    gets(str);
    for(j=i=0;str[i];i++)
        if((t=str[i]|0x20)!='a' && t!='e' && t!='i' && t!='o' && t!='u')
            str[j++]=str[i];
    str[j]='\0';
    printf("New string is \'%s\'\n",str);
    return 0;
}
