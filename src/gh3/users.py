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
    collaborators_count = _attrs.aliased(
        json_key='collaborators',
        default=_attrs.NOT_PROVIDED,
    )
    company = attr.ib(default=_attrs.NOT_PROVIDED)
    created_at = attr.ib(
        convert=_attrs.isodatetime,
        default=_attrs.NOT_PROVIDED,
    )
    disk_usage = attr.ib(default=_attrs.NOT_PROVIDED)
    email = attr.ib(default=_attrs.NOT_PROVIDED)
    followers_count = _attrs.aliased(
        json_key='followers',
        default=_attrs.NOT_PROVIDED,
    )
    following_count = _attrs.aliased(
        json_key='following',
        default=_attrs.NOT_PROVIDED,
    )
    hireable = attr.ib(default=_attrs.NOT_PROVIDED)
    location = attr.ib(default=_attrs.NOT_PROVIDED)
    name = attr.ib(default=_attrs.NOT_PROVIDED)
    owned_private_repos_count = _attrs.aliased(
        json_key='owned_private_repos',
        default=_attrs.NOT_PROVIDED,
    )
    plan = attr.ib(convert=Plan.from_dictionary, default=_attrs.NOT_PROVIDED)
    private_gists_count = _attrs.aliased(
        json_key='private_gists',
        default=_attrs.NOT_PROVIDED,
    )
    public_gists_count = _attrs.aliased(
        json_key='public_gists',
        default=_attrs.NOT_PROVIDED,
    )
    public_repos_count = _attrs.aliased(
        json_key='public_repos',
        default=_attrs.NOT_PROVIDED,
    )
    total_private_repos_count = _attrs.aliased(
        json_key='total_private_repos',
        default=_attrs.NOT_PROVIDED,
    )
    updated_at = attr.ib(
        convert=_attrs.isodatetime,
        default=_attrs.NOT_PROVIDED
    )

    @classmethod
    def from_dictionary(cls, dictionary):
        if dictionary is _attrs.NOT_PROVIDED:
            return _attrs.NOT_PROVIDED

        for attribute in attr.fields(cls):
            original_name = attribute.metadata.get('json_key')
            if original_name is not None and original_name in dictionary:
                dictionary[attribute.name] = dictionary.pop(original_name)
        return cls(**dictionary)
