# WR Beats 🎵

A modern, full-stack music beats marketplace and production platform. Buy, sell, and create beats with a secure, scalable infrastructure.

## 📋 Table of Contents

- [Features](#features)
- [Tech Stack](#tech-stack)
- [Installation](#installation)
- [Database Schema](#database-schema)
- [API Endpoints](#api-endpoints)
- [Security](#security)
- [Configuration](#configuration)
- [Contributing](#contributing)
- [License](#license)

## ✨ Features

### User Management
- 🔐 User registration and authentication (JWT-based)
- 👤 User profiles with portfolio showcase
- 🔑 Secure password hashing with bcrypt
- 📧 Email verification support

### Beats Platform
- 🎼 Upload and manage beats
- 🎧 Download beats with licensing options
- 🔍 Advanced search and filtering (genre, mood, BPM, key)
- ⭐ Review and rating system
- 📊 Analytics and sales tracking

### E-Commerce
- 🛒 Shopping cart functionality
- 💳 Secure payment processing (Stripe/PayPal)
- 📜 License management (exclusive, non-exclusive)
- 📦 Transaction history and receipts

### Admin Features
- 🛡️ Content moderation dashboard
- 👨‍💼 User management
- 📈 Revenue analytics
- 🚨 System monitoring

## 🛠️ Tech Stack

### Backend
- **Runtime:** Node.js
- **Framework:** Express.js
- **Database:** MongoDB
- **Authentication:** JWT (JSON Web Tokens)
- **Password Hashing:** bcrypt
- **Validation:** Joi

### Frontend (Recommended)
- React.js
- Axios for API calls
- Redux for state management

### Security & DevOps
- dotenv for environment variables
- CORS for cross-origin requests
- Rate limiting middleware
- Input validation & sanitization
- HTTPS/TLS encryption

## 📦 Installation

### Prerequisites
- Node.js (v14 or higher)
- MongoDB (local or Atlas)
- npm or yarn

### Setup Steps

1. **Clone the repository**
```bash
git clone https://github.com/wrbeats/wrbeats.git
cd wrbeats
```

2. **Install dependencies**
```bash
npm install
```

3. **Create environment file**
```bash
cp .env.example .env
```

4. **Configure environment variables**
```env
PORT=5000
MONGODB_URI=mongodb://localhost:27017/wrbeats
JWT_SECRET=your_super_secret_jwt_key
BCRYPT_ROUNDS=10
STRIPE_SECRET_KEY=your_stripe_key
NODE_ENV=development
CORS_ORIGIN=http://localhost:3000
```

5. **Start the server**
```bash
npm start
```

Server will run on `http://localhost:5000`

## 🗄️ Database Schema

### Users Collection
```javascript
{
  _id: ObjectId,
  username: String,
  email: String,
  password: String (hashed),
  firstName: String,
  lastName: String,
  bio: String,
  profileImage: String,
  verified: Boolean,
  role: String, // 'user', 'producer', 'admin'
  followers: [ObjectId],
  following: [ObjectId],
  createdAt: Date,
  updatedAt: Date
}
```

### Beats Collection
```javascript
{
  _id: ObjectId,
  title: String,
  description: String,
  producer: ObjectId, // Reference to Users
  genre: String,
  mood: [String],
  bpm: Number,
  key: String,
  duration: Number,
  fileUrl: String,
  previewUrl: String,
  price: Number,
  license: String, // 'exclusive', 'non-exclusive'
  tags: [String],
  downloads: Number,
  rating: Number,
  reviews: [ObjectId], // Reference to Reviews
  createdAt: Date,
  updatedAt: Date
}
```

### Transactions Collection
```javascript
{
  _id: ObjectId,
  buyer: ObjectId, // Reference to Users
  seller: ObjectId, // Reference to Users
  beat: ObjectId, // Reference to Beats
  amount: Number,
  currency: String,
  licenseType: String,
  transactionId: String,
  status: String, // 'pending', 'completed', 'failed'
  paymentMethod: String,
  createdAt: Date,
  completedAt: Date
}
```

### Reviews Collection
```javascript
{
  _id: ObjectId,
  beat: ObjectId, // Reference to Beats
  user: ObjectId, // Reference to Users
  rating: Number, // 1-5
  comment: String,
  helpful: Number,
  createdAt: Date,
  updatedAt: Date
}
```

## 🔌 API Endpoints

### Authentication
```
POST   /api/auth/register          - Register new user
POST   /api/auth/login             - Login user
POST   /api/auth/refresh-token     - Refresh JWT token
POST   /api/auth/logout            - Logout user
```

### Users
```
GET    /api/users/:id              - Get user profile
PUT    /api/users/:id              - Update user profile
GET    /api/users/:id/beats        - Get user's beats
GET    /api/users/:id/purchases    - Get user's purchases
```

### Beats
```
GET    /api/beats                  - List all beats (with filters)
GET    /api/beats/:id              - Get beat details
POST   /api/beats                  - Upload new beat (producer only)
PUT    /api/beats/:id              - Update beat details
DELETE /api/beats/:id              - Delete beat (owner only)
GET    /api/beats/:id/preview      - Stream beat preview
GET    /api/beats/search?q=query   - Search beats
```

### Transactions & Purchases
```
POST   /api/transactions           - Create purchase
GET    /api/transactions/:id       - Get transaction details
GET    /api/transactions/user/:id  - Get user transactions
POST   /api/transactions/download  - Download purchased beat
```

### Reviews
```
POST   /api/reviews                - Create review
GET    /api/reviews/beat/:id       - Get beat reviews
PUT    /api/reviews/:id            - Update review
DELETE /api/reviews/:id            - Delete review
```

## 🔒 Security

### Implemented Security Measures

1. **Authentication & Authorization**
   - JWT tokens with expiration
   - Secure password hashing (bcrypt)
   - Role-based access control (RBAC)

2. **Data Protection**
   - Input validation and sanitization
   - NoSQL injection prevention
   - XSS protection headers

3. **API Security**
   - CORS configuration
   - Rate limiting (prevent brute force)
   - API key validation
   - Request size limits

4. **File Upload Security**
   - File type validation
   - File size limits
   - Virus scanning (recommended)
   - Secure storage

5. **Data Encryption**
   - HTTPS/TLS for all communications
   - Sensitive data encryption at rest
   - Secure token storage

### Best Practices

- ✅ Never commit `.env` files
- ✅ Use environment variables for secrets
- ✅ Implement HTTPS in production
- ✅ Regular security audits
- ✅ Keep dependencies updated
- ✅ Use strong JWT secrets
- ✅ Implement logging and monitoring

## ⚙️ Configuration

### Environment Variables

```env
# Server
PORT=5000
NODE_ENV=production

# Database
MONGODB_URI=mongodb+srv://user:password@cluster.mongodb.net/wrbeats

# Authentication
JWT_SECRET=your_long_random_secret_key_here
JWT_EXPIRE=7d
BCRYPT_ROUNDS=10

# Payment
STRIPE_SECRET_KEY=sk_live_xxxxx
PAYPAL_CLIENT_ID=xxxxx

# File Storage
STORAGE_TYPE=s3 # or local
AWS_BUCKET_NAME=wrbeats-uploads
AWS_REGION=us-east-1

# CORS
CORS_ORIGIN=https://wrbeats.com

# Email
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USER=your_email@gmail.com
SMTP_PASS=your_app_password
```

## 🤝 Contributing

We welcome contributions! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Code Standards
- Follow ESLint configuration
- Write meaningful commit messages
- Add tests for new features
- Update documentation

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

## 📞 Support

For issues, questions, or suggestions:
- Open an issue on GitHub
- Contact: support@wrbeats.com
- Discord: [Join our community](https://discord.gg/wrbeats)

## 🚀 Roadmap

- [ ] Mobile app (iOS & Android)
- [ ] Advanced beat analytics
- [ ] Collaboration features
- [ ] Live production stream
- [ ] Marketplace recommendations AI
- [ ] Multi-language support

---

**Happy producing! 🎵🎧**

Made with ❤️ by WR Beats Team
