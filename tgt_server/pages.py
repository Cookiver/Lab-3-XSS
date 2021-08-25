from typing import Optional

from fastapi.templating import Jinja2Templates

from config import settings


templates = Jinja2Templates(directory="templates")
templates.env.autoescape = settings.autoescape


async def user_profiles_page(request, user_profiles, search_value: Optional[str] = ''):
    return templates.TemplateResponse(
        name='user_profiles.html',
        context={
            'request': request,
            'search_value': search_value,
            'profiles': [
                dict(name=profile.fields['name'], url=f'/user-profiles/{k}')
                for k, profile in user_profiles.items()]
        },
        headers={'X-XSS-Protection': '0'}
    )


async def user_profile_page(request, profile, edit):
    return templates.TemplateResponse(
        name=f"profile{'_form' if edit else ''}.html",
        context={
            'request': request,
            'profile': profile
        }
    )


async def edited_user_profile_unsafe(_id, request, profile):
    return templates.TemplateResponse(
        name=f"profile.html",
        context={
            'request': request,
            'profile': profile
        },
        headers={'X-XSS-Protection': '0'}
    )
