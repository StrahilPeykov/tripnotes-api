from fastapi import HTTPException, status

class TripNotesException:
    """Custom exception class for TripNotes API"""
    
    @staticmethod
    def not_found(detail: str = "Resource not found"):
        """Return 404 Not Found exception"""
        return HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=detail
        )
    
    @staticmethod
    def unauthorized(detail: str = "Not authorized to access this resource"):
        """Return 401 Unauthorized exception"""
        return HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    @staticmethod
    def forbidden(detail: str = "Access forbidden"):
        """Return 403 Forbidden exception"""
        return HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail
        )
    
    @staticmethod
    def bad_request(detail: str = "Bad request"):
        """Return 400 Bad Request exception"""
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail
        )