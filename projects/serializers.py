from rest_framework import serializers
from .models import Project, ProjectMember


class ProjectMembersSerializer(serializers.ModelSerializer):
      class Meta:
            model = ProjectMember
            fields = '__all__'


class ProjectSerializer(serializers.ModelSerializer):
      members = ProjectMembersSerializer(many=True, required=False)

      class Meta:
            model = Project
            fields = '__all__'


      def create(self, validated_data):
            # Extract members data
            members_data = validated_data.pop('members', [])

            # Create project
            project = Project.objects.create(**validated_data)

            # Create associated members
            for member_data in members_data:
                  ProjectMember.objects.create(project=project, **member_data)
            
            return project
      

      def update(self, instance, validated_data):
            # Extract members data
            members_data = validated_data.pop('members', [])
            
            # Update project
            for attr, value in validated_data.items():
                  setattr(instance, attr, value)
            instance.save()

            # Update associated members
            instance.projectmembers_set.all().delete()  # Remove all existing members
            for member_data in members_data:
                  ProjectMember.objects.create(project=instance, **member_data)

            return instance
            

