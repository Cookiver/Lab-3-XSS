from typing import Optional
from uuid import UUID

from fastapi import Request, HTTPException
from fastapi import Form

from fastapi.staticfiles import StaticFiles
from fastapi_offline import FastAPIOffline

from config import settings
from data import user_profile_data
from exercises.ex1 import update_user_profile, search_profiles
from pages import user_profiles_page, user_profile_page, edited_user_profile_unsafe

app = FastAPIOffline()
app.mount("/static",  StaticFiles(directory="static"), name="static")


@app.get("/user-profiles")
async def user_profiles(request: Request, name: Optional[str] = ''):
    profiles = search_profiles(name=name) if name else user_profile_data
    if 'json' in request.headers.get('accept', 'html/text'):
        return profiles
    return await user_profiles_page(request, profiles, search_value=name)


@app.get("/user-profiles/{_id}")
async def user_profile(request: Request, _id: UUID, edit: Optional[bool] = False):
    if _id not in user_profile_data:
        raise HTTPException(status_code=404, detail="Profile not found.")
    profile = user_profile_data[_id]
    return await user_profile_page(request, profile, edit)


@app.post("/user-profiles/{_id}")
async def post_user_profile(request: Request, _id: UUID, name: str = Form(...), address: str = Form(...)):
    if _id not in user_profile_data:
        raise HTTPException(status_code=404, detail="Profile not found.")

    edited_profile = await update_user_profile(_id, address, name)

    if 'json' in request.headers.get('accept', 'html/text'):
        return edited_profile

    return await (edited_user_profile_unsafe(request, edited_profile) if settings.unsafe_edit_pages
                  else user_profiles(request))
