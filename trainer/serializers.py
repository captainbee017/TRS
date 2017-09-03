from rest_framework import serializers
from trainer.models import TrainerIntroduction


class TrainerIntroductionSerializer(serializers.ModelSerializer):

	class Meta:
		model = TrainerIntroduction
		fields = ('id', 'user', 'headline', 'current_position', 'address', 'summary')