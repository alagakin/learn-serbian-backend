from rest_framework import serializers
from words.models import SavedWord, Word, TextTranslation


class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word
        fields = '__all__'


class SaveWordCreateSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = SavedWord
        fields = '__all__'


class TextSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    content = serializers.CharField()

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # todo lang
        try:
            translation = TextTranslation.objects.get(text=instance,
                                                      lang='ru').content
        except TextTranslation.DoesNotExist:
            translation = None

        representation['translation'] = translation
        return representation


class TextsOfWithWordSerializer(serializers.ModelSerializer):
    title = serializers.CharField()
    texts = TextSerializer(many=True, read_only=True)

    class Meta:
        model = Word
        fields = ['title', 'texts']


class TranslationsForWordSerializer(serializers.Serializer):
    title = serializers.CharField()
    lang = serializers.CharField()


class WordTranslationSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    title = serializers.CharField()
    topics = serializers.CharField()
    texts_count = serializers.IntegerField(source='texts.count')
    audio_link = serializers.CharField()

    def to_representation(self, instance):
        from topics.serializers import TopicsForWordSerializer

        representation = super().to_representation(instance)
        # todo lang
        translations = instance.translations.filter(lang='ru')
        topics = instance.topics.all()
        serialized_translations = TranslationsForWordSerializer(translations,
                                                                many=True)
        serialized_topics = TopicsForWordSerializer(topics,
                                                    many=True)
        representation['translation'] = serialized_translations.data
        representation['topics'] = serialized_topics.data

        return representation


class SavedWordsIds(serializers.Serializer):
    id = serializers.IntegerField(source='word.id')


class SavedWordListSerializer(serializers.ModelSerializer):
    word = WordTranslationSerializer(read_only=True)

    class Meta:
        model = SavedWord
        fields = '__all__'


class ProgressSerializer(serializers.Serializer):
    id = serializers.SerializerMethodField()
    cnt = serializers.SerializerMethodField()

    def get_id(self, instance):
        return instance.word.id

    def get_cnt(self, instance):
        return instance.repetition_count
