# Gym App - API Reference

## Authentication

### Register a New User
```
POST /api/v1/auth/register
```

**Request Body:**
```json
{
  "email": "user@example.com",
  "password": "securepassword123",
  "full_name": "John Doe"
}
```

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false
}
```

### Login
```
POST /api/v1/auth/login
```

**Form Data:**
- username: user@example.com
- password: securepassword123

**Response:**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

### Refresh Token
```
POST /api/v1/auth/refresh
```

**Request Body:**
```json
{
  "refresh_token": "your_refresh_token_here"
}
```

**Response:**
```json
{
  "access_token": "new_access_token_here",
  "token_type": "bearer"
}
```

## Users

### Get Current User Profile
```
GET /api/v1/users/me
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": true,
  "is_superuser": false
}
```

### Update Current User Profile
```
PUT /api/v1/users/me
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "email": "newemail@example.com",
  "full_name": "John Doe Updated",
  "password": "newpassword123"
}
```

**Response:**
```json
{
  "id": 1,
  "email": "newemail@example.com",
  "full_name": "John Doe Updated",
  "is_active": true,
  "is_superuser": false
}
```

## Workout Routines

### List User's Workout Routines
```
GET /api/v1/routines
```

**Headers:**
- Authorization: Bearer <access_token>

**Query Parameters:**
- skip: number (default: 0)
- limit: number (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "name": "Beginner Strength Routine",
    "description": "A full-body routine for beginners",
    "is_public": false,
    "user_id": 1,
    "created_at": "2023-01-15T10:30:00Z",
    "updated_at": "2023-01-15T10:30:00Z"
  }
]
```

### Create a New Workout Routine
```
POST /api/v1/routines
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "name": "Advanced Hypertrophy Program",
  "description": "Hypertrophy-focused routine for intermediate lifters",
  "is_public": false
}
```

**Response:**
```json
{
  "id": 2,
  "name": "Advanced Hypertrophy Program",
  "description": "Hypertrophy-focused routine for intermediate lifters",
  "is_public": false,
  "user_id": 1,
  "created_at": "2023-01-16T14:22:00Z",
  "updated_at": "2023-01-16T14:22:00Z"
}
```

### Get Specific Workout Routine
```
GET /api/v1/routines/{routine_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 1,
  "name": "Beginner Strength Routine",
  "description": "A full-body routine for beginners",
  "is_public": false,
  "user_id": 1,
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2023-01-15T10:30:00Z"
}
```

### Update Workout Routine
```
PUT /api/v1/routines/{routine_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "name": "Updated Routine Name",
  "description": "Updated description",
  "is_public": true
}
```

**Response:**
```json
{
  "id": 1,
  "name": "Updated Routine Name",
  "description": "Updated description",
  "is_public": true,
  "user_id": 1,
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2023-01-16T16:45:00Z"
}
```

### Delete Workout Routine
```
DELETE /api/v1/routines/{routine_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 1,
  "name": "Beginner Strength Routine",
  "description": "A full-body routine for beginners",
  "is_public": false,
  "user_id": 1,
  "created_at": "2023-01-15T10:30:00Z",
  "updated_at": "2023-01-15T10:30:00Z"
}
```

## Exercises

### List All Exercises
```
GET /api/v1/exercises
```

**Headers:**
- Authorization: Bearer <access_token>

**Query Parameters:**
- muscle_group: string (e.g., "chest", "back", "legs")
- equipment_needed: string (e.g., "barbell", "dumbbells", "bodyweight")
- skip: number (default: 0)
- limit: number (default: 100)

**Response:**
```json
[
  {
    "id": 1,
    "name": "Barbell Bench Press",
    "description": "Compound chest exercise",
    "muscle_group": "chest",
    "equipment_needed": "barbell, bench"
  },
  {
    "id": 2,
    "name": "Pull-ups",
    "description": "Upper body pulling exercise",
    "muscle_group": "back",
    "equipment_needed": "pull-up bar"
  }
]
```

### Get Specific Exercise
```
GET /api/v1/exercises/{exercise_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 1,
  "name": "Barbell Bench Press",
  "description": "Compound chest exercise",
  "muscle_group": "chest",
  "equipment_needed": "barbell, bench"
}
```

## Workout Sessions

### List User's Workout Sessions
```
GET /api/v1/sessions
```

**Headers:**
- Authorization: Bearer <access_token>

**Query Parameters:**
- skip: number (default: 0)
- limit: number (default: 100)
- start_date: string (ISO date format, optional)
- end_date: string (ISO date format, optional)

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "workout_routine_id": 1,
    "date": "2023-01-16T15:30:00Z",
    "duration": 45,
    "notes": "Felt strong today",
    "completed": true,
    "created_at": "2023-01-16T15:30:00Z"
  }
]
```

### Create a New Workout Session
```
POST /api/v1/sessions
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "workout_routine_id": 1,
  "date": "2023-01-16T15:30:00Z",
  "duration": 45,
  "notes": "Felt strong today"
}
```

**Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "workout_routine_id": 1,
  "date": "2023-01-16T15:30:00Z",
  "duration": 45,
  "notes": "Felt strong today",
  "completed": false,
  "created_at": "2023-01-16T15:30:00Z"
}
```

### Get Specific Workout Session
```
GET /api/v1/sessions/{session_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "workout_routine_id": 1,
  "date": "2023-01-16T15:30:00Z",
  "duration": 45,
  "notes": "Felt strong today",
  "completed": false,
  "created_at": "2023-01-16T15:30:00Z"
}
```

### Update Workout Session
```
PUT /api/v1/sessions/{session_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "date": "2023-01-16T16:00:00Z",
  "duration": 50,
  "notes": "Felt strong today - added extra set",
  "completed": true
}
```

**Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "workout_routine_id": 1,
  "date": "2023-01-16T16:00:00Z",
  "duration": 50,
  "notes": "Felt strong today - added extra set",
  "completed": true,
  "created_at": "2023-01-16T15:30:00Z",
  "updated_at": "2023-01-16T16:00:00Z"
}
```

### Delete Workout Session
```
DELETE /api/v1/sessions/{session_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 1,
  "user_id": 1,
  "workout_routine_id": 1,
  "date": "2023-01-16T15:30:00Z",
  "duration": 45,
  "notes": "Felt strong today",
  "completed": false,
  "created_at": "2023-01-16T15:30:00Z"
}
```

## Sets

### List Sets for a Workout Session
```
GET /api/v1/sessions/{session_id}/sets
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
[
  {
    "id": 1,
    "workout_session_id": 1,
    "exercise_id": 1,
    "reps": 10,
    "weight": 60.0,
    "order": 1
  },
  {
    "id": 2,
    "workout_session_id": 1,
    "exercise_id": 1,
    "reps": 8,
    "weight": 65.0,
    "order": 2
  }
]
```

### Add a Set to a Workout Session
```
POST /api/v1/sessions/{session_id}/sets
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "exercise_id": 1,
  "reps": 12,
  "weight": 55.0,
  "order": 3
}
```

**Response:**
```json
{
  "id": 3,
  "workout_session_id": 1,
  "exercise_id": 1,
  "reps": 12,
  "weight": 55.0,
  "order": 3
}
```

### Update a Set
```
PUT /api/v1/sessions/{session_id}/sets/{set_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "reps": 15,
  "weight": 50.0,
  "order": 3
}
```

**Response:**
```json
{
  "id": 3,
  "workout_session_id": 1,
  "exercise_id": 1,
  "reps": 15,
  "weight": 50.0,
  "order": 3
}
```

### Delete a Set
```
DELETE /api/v1/sessions/{session_id}/sets/{set_id}
```

**Headers:**
- Authorization: Bearer <access_token>

**Response:**
```json
{
  "id": 3,
  "workout_session_id": 1,
  "exercise_id": 1,
  "reps": 12,
  "weight": 55.0,
  "order": 3
}
```

## Progress Tracking

### Get User's Progress Metrics
```
GET /api/v1/progress
```

**Headers:**
- Authorization: Bearer <access_token>

**Query Parameters:**
- metric_type: string (e.g., "weight", "body_fat") - optional
- start_date: string (ISO date format) - optional
- end_date: string (ISO date format) - optional

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "metric_type": "weight",
    "value": 75.5,
    "date": "2023-01-01T00:00:00Z",
    "created_at": "2023-01-01T08:00:00Z"
  },
  {
    "id": 2,
    "user_id": 1,
    "metric_type": "weight",
    "value": 74.8,
    "date": "2023-01-15T00:00:00Z",
    "created_at": "2023-01-15T08:00:00Z"
  }
]
```

### Log a New Progress Metric
```
POST /api/v1/progress
```

**Headers:**
- Authorization: Bearer <access_token>

**Request Body:**
```json
{
  "metric_type": "weight",
  "value": 74.0,
  "date": "2023-01-31T00:00:00Z"
}
```

**Response:**
```json
{
  "id": 3,
  "user_id": 1,
  "metric_type": "weight",
  "value": 74.0,
  "date": "2023-01-31T00:00:00Z",
  "created_at": "2023-01-31T08:00:00Z"
}
```

### Get Progress for Specific Metric Type
```
GET /api/v1/progress/{metric_type}
```

**Headers:**
- Authorization: Bearer <access_token>

**Query Parameters:**
- start_date: string (ISO date format) - optional
- end_date: string (ISO date format) - optional

**Response:**
```json
[
  {
    "id": 1,
    "user_id": 1,
    "metric_type": "weight",
    "value": 75.5,
    "date": "2023-01-01T00:00:00Z",
    "created_at": "2023-01-01T08:00:00Z"
  },
  {
    "id": 2,
    "user_id": 1,
    "metric_type": "weight",
    "value": 74.8,
    "date": "2023-01-15T00:00:00Z",
    "created_at": "2023-01-15T08:00:00Z"
  },
  {
    "id": 3,
    "user_id": 1,
    "metric_type": "weight",
    "value": 74.0,
    "date": "2023-01-31T00:00:00Z",
    "created_at": "2023-01-31T08:00:00Z"
  }
]
```

## Admin Endpoints

### Get All Users (Admin Only)
```
GET /api/v1/admin/users
```

**Headers:**
- Authorization: Bearer <access_token> (must be superuser)

**Response:**
```json
[
  {
    "id": 1,
    "email": "user@example.com",
    "full_name": "John Doe",
    "is_active": true,
    "is_superuser": false
  },
  {
    "id": 2,
    "email": "admin@example.com",
    "full_name": "Admin User",
    "is_active": true,
    "is_superuser": true
  }
]
```

### Deactivate/Activate User (Admin Only)
```
PUT /api/v1/admin/users/{user_id}/deactivate
```

**Headers:**
- Authorization: Bearer <access_token> (must be superuser)

**Response:**
```json
{
  "id": 1,
  "email": "user@example.com",
  "full_name": "John Doe",
  "is_active": false,
  "is_superuser": false
}
```

### Delete User (Admin Only)
```
DELETE /api/v1/admin/users/{user_id}
```

**Headers:**
- Authorization: Bearer <access_token> (must be superuser)

**Response:**
```json
{
  "message": "User deleted successfully"
}
```

## Error Responses

### Validation Error (422)
```json
{
  "detail": [
    {
      "loc": ["body", "email"],
      "msg": "value is not a valid email address",
      "type": "value_error.email"
    }
  ]
}
```

### Authentication Error (401)
```json
{
  "detail": "Not authenticated"
}
```

### Authorization Error (403)
```json
{
  "detail": "Not enough permissions"
}
```

### Not Found (404)
```json
{
  "detail": "Resource not found"
}
```

### Server Error (500)
```json
{
  "detail": "Internal server error"
}
```