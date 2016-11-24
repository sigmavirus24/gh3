import attr
import uritemplate

from gh3 import _attrs


@attr.s
class Plan(object):
    name = attr.ib()
    space = attr.ib(convert=int)
    private_repos = attr.ib(convert=int)
    collaborators = attr.ib(convert=int)

    @classmethod
    def from_dictionary(cls, dictionary):
        if dictionary is _attrs.NOT_PROVIDED:
            return _attrs.NOT_PROVIDED
        return cls(**dictionary)


@attr.s
class User(object):
    avatar_url = attr.ib()
    events_url = attr.ib(convert=uritemplate.URITemplate)
    followers_url = attr.ib()
    following_url = attr.ib(convert=uritemplate.URITemplate)
    gists_url = attr.ib(convert=uritemplate.URITemplate)
    gravatar_id = attr.ib()
    html_url = attr.ib()
    id = attr.ib(convert=int)
    login = attr.ib()
    organizations_url = attr.ib()
    received_events_url = attr.ib()
    repos_url = attr.ib()
    site_admin = attr.ib(validator=attr.validators.instance_of(bool))
    starred_url = attr.ib(convert=uritemplate.URITemplate)
    subscriptions_url = attr.ib()
    type = attr.ib()
    url = attr.ib()

    bio = attr.ib(default=_attrs.NOT_PROVIDED)
    blog = attr.ib(default=_attrs.NOT_PROVIDED)
    collaborators_count = attr.ib(default=_attrs.NOT_PROVIDED)
    company = attr.ib(default=_attrs.NOT_PROVIDED)
    created_at = attr.ib(
        convert=_attrs.isodatetime,
        default=_attrs.NOT_PROVIDED,
    )
    disk_usage = attr.ib(default=_attrs.NOT_PROVIDED)
    email = attr.ib(default=_attrs.NOT_PROVIDED)
    followers_count = attr.ib(default=_attrs.NOT_PROVIDED)
    following_count = attr.ib(default=_attrs.NOT_PROVIDED)
    hireable = attr.ib(default=_attrs.NOT_PROVIDED)
    location = attr.ib(default=_attrs.NOT_PROVIDED)
    name = attr.ib(default=_attrs.NOT_PROVIDED)
    owned_private_repos_count = attr.ib(default=_attrs.NOT_PROVIDED)
    plan = attr.ib(convert=Plan.from_dictionary, default=_attrs.NOT_PROVIDED)
    private_gists_count = attr.ib(default=_attrs.NOT_PROVIDED)
    public_gists_count = attr.ib(default=_attrs.NOT_PROVIDED)
    public_repos_count = attr.ib(default=_attrs.NOT_PROVIDED)
    total_private_repos_count = attr.ib(default=_attrs.NOT_PROVIDED)
    updated_at = attr.ib(
        convert=_attrs.isodatetime,
        default=_attrs.NOT_PROVIDED
    )

    _aliases = {
        'collaborators': 'collaborators_count',
        'followers': 'followers_count',
        'following': 'following_count',
        'owned_private_repos': 'owned_private_repos_count',
        'private_gists': 'private_gists_count',
        'public_gists': 'public_gists_count',
        'public_repos': 'public_repos_count',
        'total_private_repos': 'total_private_repos_count',
    }

    @classmethod
    def from_dictionary(cls, dictionary):
        for original_name, new_name in cls._aliases.items():
            if original_name in dictionary:
                dictionary[new_name] = dictionary.pop(original_name)
        return cls(**dictionary)
