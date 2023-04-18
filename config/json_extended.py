import json


class ExtendedJSONEncoder(json.JSONEncoder):
    # 인코딩시 집합자료 구조일 경우, 사전타입으로 변환.
    def default(self, obj):
        if isinstance(obj, set):
            return {"__set__": True, "values": tuple(obj)}
        return obj


class ExtendedJSONDecoder(json.JSONDecoder):
    # 커스텀한 집합자료구조일 경우, 집합으로 변환.
    def __init__(self, **kwargs):
        kwargs.setdefault("object_hook", self._object_hook)
        super().__init__(**kwargs)
    
    @staticmethod
    def _object_hook(dct):
        if '__set__' in dct:
            return set(dct['values'])
        return dct
