const path = require('path')
const express = require('express')
const passport = require('passport')
const app = express()
const fileUpload = require('express-fileupload-sha256')
const cookieSession = require('cookie-session')

const rootRoutes = require('./routes/root')
const analysisRoutes = require('./analysis/index')
const authRoutes = require('./auth/index').router

const tempDir = path.resolve(__dirname, './tmp/')
const port = process.env.PORT || 3000
const inDevMode = process.env.NODE_ENV === 'dev'
const staticFileOptions = {
  // Will advise user agents to nto download files during maxAge (defautl)
  immutable: true
}

const uploadMiddleWare = fileUpload({
  createParentPath: true,
  useTempFiles: true,
  tempFileDir: tempDir,
  debug: inDevMode
})

app.use(allowCORS)
app.use(uploadMiddleWare)
app.use(cookieSession({
  // milliseconds of a day
  maxAge: 24*60*60*1000,
  keys:['somekeys']
}));
app.use(passport.initialize())
app.use(passport.session())

app.use('/', rootRoutes)
app.use('/analysis', analysisRoutes)
app.use('/', authRoutes)
app.use('/public', express.static('data/public/analysis', staticFileOptions))

app.listen(port, logStart)

function logStart () {
  console.log(`App is listening on port ${port}`)
}

function allowCORS (req, res, next) {
  const clientAppOrigin = req.get('origin') || 'http://130.60.156.181:8081'
  res.header('Access-Control-Allow-Origin', clientAppOrigin)
  res.header('Access-Control-Allow-Methods', 'GET,POST,DELETE,HEAD,OPTIONS')
  res.header('Access-Control-Allow-Headers', 'Origin, X-Requested-With, Content-Type, Accept')
  res.header('Access-Control-Allow-Credentials', 'true')
  next();
}
