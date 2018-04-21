from django.core.exceptions import ObjectDoesNotExist
from .models import Profile

def save_avatar(backend, user, response, *args, **kwargs):
	try:
		profile = Profile.objects.get(user_id=user.id)
	except Profile.DoesNotExist:
		profile = Profile(user_id=user.id)

	if backend.name == 'google-oauth2':
		profile.avatar = response['image'].get('url')

	profile.save()
