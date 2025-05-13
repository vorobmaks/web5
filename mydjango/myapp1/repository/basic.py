from django.core.exceptions import ObjectDoesNotExist

class BaseRepository:
    model = None

    @classmethod
    def get(cls, pk):
        try:
            return cls.model.objects.get(pk=pk)
        except ObjectDoesNotExist:
            return None

    @classmethod
    def get_by_field(cls, field_name, value):
        try:
            return cls.model.objects.get(**{field_name: value})
        except ObjectDoesNotExist:
            return None

    @classmethod
    def create(cls, **kwargs):
        return cls.model.objects.create(**kwargs)

    @classmethod
    def delete(cls, instance):
        instance.delete()

    @classmethod
    def delete_by_team_name(cls, team_name):
        team_instance = cls.get_by_field('team_name', team_name)
        if team_instance:
            cls.delete(team_instance)
        else:
            print(f"Team with name '{team_name}' does not exist.")

    @classmethod
    def all(self):
        return self.model.objects.all()

