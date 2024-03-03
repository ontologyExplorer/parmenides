from __future__ import annotations

from typing import List

from pydantic import BaseModel


class TagItem(BaseModel):
    system: str
    code: str
    display: str


class Meta(BaseModel):
    lastUpdated: str
    tag: List[TagItem]


class LinkItem(BaseModel):
    relation: str
    url: str


class TagItem1(BaseModel):
    system: str
    code: str
    display: str


class Meta1(BaseModel):
    versionId: str
    lastUpdated: str
    profile: List[str]
    tag: List[TagItem1]


class IdentifierItem(BaseModel):
    system: str
    value: str


class Resource(BaseModel):
    resourceType: str
    id: str
    meta: Meta1
    url: str
    identifier: List[IdentifierItem]
    version: str
    name: str
    status: str
    experimental: bool
    date: str
    publisher: str


class EntryItem(BaseModel):
    fullUrl: str
    resource: Resource


class Model(BaseModel):
    resourceType: str
    id: str
    meta: Meta
    type: str
    total: int
    link: List[LinkItem]
    entry: List[EntryItem]
