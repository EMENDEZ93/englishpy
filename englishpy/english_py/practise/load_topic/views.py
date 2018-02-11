from django.shortcuts import render, get_object_or_404

from ..types import TopicTypes
from ..models import Topic, Present, Vocabulary

def topic(request, id_topic, template_name='practise/load_topic/topic.html', ):
    data = dict()
    topic = get_object_or_404(Topic,pk=id_topic)

    words = list()

    if topic.name == TopicTypes.VERBS:
        for present in Present.objects.all():
            if not Vocabulary.objects.filter(word=present.verb, routine=topic).exists():
                Vocabulary.objects.create(word=present.verb, routine=topic)
                words.append(present.verb)

    data['topic'] = topic
    data['words'] = words
    return render(request,template_name, data)


def topic_delete(request, id_topic, template_name='practise/load_topic/delete.html', ):
    data = dict()
    topic = get_object_or_404(Topic,pk=id_topic)

    data['topic'] = topic
    Vocabulary.objects.filter(routine=topic).delete()
    return render(request,template_name, data)
