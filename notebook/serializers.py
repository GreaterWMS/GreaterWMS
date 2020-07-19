from rest_framework import serializers

class NoteBookSerializers(serializers.Serializer):
    id = serializers.CharField(read_only=True)
    icon = serializers.CharField(read_only=True)
    icon_color = serializers.CharField(read_only=True)
    title = serializers.CharField(read_only=True)
    desc = serializers.CharField(read_only=True)
    progress = serializers.CharField(read_only=True)
    note_day = serializers.DateField(read_only=True, format='%Y年%m月%d日')

class NoteBookEventSerializers(serializers.Serializer):
    note_day = serializers.DateField(read_only=True, format='%Y/%m/%d')
