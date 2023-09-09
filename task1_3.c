#include <stdio.h>
#include <stdlib.h>
#include <string.h>
typedef struct
{
    int  id;
    char name[100];
}tasks;
tasks task_arr[100];
int tasks_cntr=0;
void load() //loading from file the tasks
{
    FILE *f=fopen("tasks.txt","r");
    if(f==NULL)
    {
        printf("ERROR OPENING THE FILE");
        exit(0);
    }
    while(!feof(f))
    {
        fscanf(f,"%d %s\n",&task_arr[tasks_cntr].id,task_arr[tasks_cntr].name);
        tasks_cntr++;
    }
    fclose(f);
}
void delete_task()
{
    printf("Enter task ID to remove: ");
    int id;
    scanf("%d",&id);
    if(id>tasks_cntr)
    {
        printf("invalid id\n");
        getchar();
        option_select();
    }
    else
    {
        int i;
        id--;
        for(i=id;i<tasks_cntr;i++)
        {
            task_arr[i]=task_arr[i+1];
            task_arr[i].id--;
        }
        tasks_cntr--;
    }
    getchar();
    option_select();
}
void view_tasks()
{
    if(tasks_cntr==0)
        printf("no tasks to view\n");
    int i;
    printf("Current Tasks:\n");
    for(i=0;i<tasks_cntr;i++)
    {
        printf("Task Id: %d\n",task_arr[i].id);
        printf("Description: %s",task_arr[i].name);
        printf("\n\n");
    }
    option_select();
}
void add_task()
{
    printf("Enter task description: ");
    gets(task_arr[tasks_cntr].name);
    task_arr[tasks_cntr].id=tasks_cntr+1;
    tasks_cntr++;
    printf("\nTask added successfully!\n");
    option_select();

}
void save() //save data to the file
{
    int index;
    FILE *f=fopen("tasks.txt","w");
    for(index=0; index<tasks_cntr; index++)
    {
        if(index!=tasks_cntr-1)
            fprintf(f,"%d %s\n",task_arr[index].id,task_arr[index].name);
        else
             fprintf(f,"%d %s",task_arr[index].id,task_arr[index].name);
    }
    fclose(f);
}
void option_select()
{
    printf("Select an option: ");
    char option[10];
    gets(option);
    if(!strcmp(option,"1"))
    {
        add_task();
    }
    else if(!strcmp(option,"2"))
    {
        view_tasks();
    }
    else if(!strcmp(option,"3"))
    {
        delete_task();
    }
    else if(!strcmp(option,"4"))
    {
        printf("Exiting Minions Task Manager. Have a great day!");
        save();
        exit(0);
    }
    else
    {
        printf("\nunknown option!!!please try again\n");
        option_select();
    }
}
void menu()
{
    printf("Minions Task Manager\n");
    printf("1. Add Task\n2. View Tasks\n3. Remove Task\n4. Exit\n");
}
int main()
{
    load();
    menu();
    option_select();

    return 0;
}
