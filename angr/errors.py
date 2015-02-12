class AngrError(Exception):
    pass

class AngrMemoryError(AngrError):
    pass

class AngrTranslationError(AngrError):
    pass

class AngrExitError(AngrError):
    pass

class AngrPathError(AngrError):
    pass

class AngrVFGError(AngrError):
    pass

class AngrInvalidArgumentError(AngrError):
    pass

class AngrSurveyorError(AngrError):
    pass

class AngrAnalysisError(AngrError):
    pass

class PathUnreachableError(AngrError):
    pass

class AngrBladeError(AngrError):
    pass

class AngrAnnotatedCFGError(AngrError):
    pass

class AngrCFGError(AngrError):
    pass