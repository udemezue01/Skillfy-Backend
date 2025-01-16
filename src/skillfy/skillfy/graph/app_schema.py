import graphene
from graphene_django.types import DjangoObjectType


from django.contrib.auth import get_user_model
User = get_user_model()


# Local Model Import

from post.models import Post
from job.models import Job
from userprofile.models import Profile


class AccountType(DjangoObjectType):

	class Meta:

		model = User

class PostType(DjangoObjectType):

	class Meta:

		model = Post


class ProfileType(DjangoObjectType):

	class Meta:

		model = Profile



class JobType(DjangoObjectType):

	image 	= graphene.String()

	class Meta:

		model = Job

	def resolve_image(self, info):
		return info.context.build_absolute_uri(self.image.url)




class Query(object):


	# The User Detail
	me 				= 	graphene.Field(AccountType)

	# The Profile Detail

	Profile 		=  	graphene.Field(ProfileType, id = graphene.Int())

	# The Post List and Detail

	posts 			= 	graphene.List(PostType)
	post 			= 	graphene.Field(PostType, id = graphene.Int())

	# The Portfolio List and Detail

	jobs 		= 	graphene.List(JobType)
	job 		= 	graphene.Field(JobType, id = graphene.Int())


	def resolve_me(root, info, **kwargs):

		user  =  info.context.user


	def resolve_posts(root, info, **kwargs):

		return Post.objects.all()

	def resolve_post(root, info, **kwargs):

		id = kwargs.get('id')

		if id is not None:

			return Post.objects.get(pk = id)

		return None

	def resolve_jobs(root, info, **kwargs):

		return Job.objects.all()

	def resolve_job(root, info, **kwargs):

		id = kwargs.get('id')

		if id is not None:

			return Job.objects.get(pk = id)

		return None







