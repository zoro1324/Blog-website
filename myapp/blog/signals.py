
from django.contrib.auth.models import Permission,Group

def Create_Group(sender,**kwargs):
    try:

        reader_group,created = Group.objects.get_or_create(name = "Reader")
        writer_group,created = Group.objects.get_or_create(name = "Writer")
        editor_group,created = Group.objects.get_or_create(name = "Editor")
        
        reader_permission = [
            Permission.objects.get(codename = "view_post")
        ]
        
        writer_permission = [
            Permission.objects.get(codename = "view_post"),
            Permission.objects.get(codename = "add_post"),
            Permission.objects.get(codename = "change_post"),
            Permission.objects.get(codename = "delete_post"),
        ]
        publish,create =Permission.objects.get_or_create(name = "Can Publish Post",content_type_id = 8,codename = "publish_post")

        editor_permission = [
            Permission.objects.get(codename = "view_post"),
            Permission.objects.get(codename = "change_post"),
            Permission.objects.get(codename = "add_post"),
            publish,
            Permission.objects.get(codename = "delete_post"),
        ]

        writer_group.permissions.set(writer_permission)
        reader_group.permissions.set(reader_permission)
        editor_group.permissions.set(editor_permission)
        print("Group Created")
    
    except Exception as e:
        print(e)