import Request from '@/api/common'

// auth
import * as auths from '@/api/auths'
export const auth = auths

// systems
export const user = new Request('/sys/user/')
export const group = new Request('/sys/group/')
export const role = new Request('/sys/role/')
export const menu = new Request('/sys/menu/')
export const perm = new Request('/sys/perm/')

// tools
export const audit = new Request('/tool/audit/')
export const simple = new Request('/tool/simple/')

// notices
export const mail = new Request('/notice/mail/')
export const telegram = new Request('/notice/telegram/')

// celery_task
export const crontab = new Request('/celery_task/crontab/')
export const task = new Request('/celery_task/task/')
export const periodictask = new Request('/celery_task/periodictask/')
export const taskresult = new Request('/celery_task/taskresult/')

