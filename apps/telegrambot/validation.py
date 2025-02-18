from pydantic import BaseModel, ValidationError, field_validator, HttpUrl

import logging

logger = logging.getLogger(__name__)

class Definition(BaseModel):
    definition: str
    synonyms: list[str] | None
    antonyms: list[str] | None
    example: str | None
    
    
class Meanings(BaseModel):
    part_of_speech: str
    definitions: list[Definition]
    synonyms: list[str] | None
    antonyms: list[str] | None
    
    
class Phonetic(BaseModel):
    audio: HttpUrl | None
    
class WordValidation(BaseModel):
    word: str
    meanings: list[Meanings]
    phonetics: list[Phonetic]
    
    
    def validate_json_create_dict(json_data: dict) -> dict:
        try:
            word = WordValidation.model_validate(json_data)
            logger.info(f"Validation success:{word.model_dump()}")
            return word.model_dump()
        
        except ValidationError as e:
            logger.warning(f"Validation Error:{e}")
        
        except Exception  as e:
            logger(f"Unexpected Error: {e}")
        
