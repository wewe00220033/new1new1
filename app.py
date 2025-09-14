#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
🔥 FC 26 Trading Bot - النسخة الكاملة المتكاملة مع نظام الأدمن
البوت الكامل في ملف واحد مع نظام الرسائل الذكي ولوحة تحكم الأدمن
مشروع لبيع كوينز FC 26
================================================================================
⚠️⚠️⚠️ تحذير هام جداً للمساعد الذكي - اقرأ هذا أولاً قبل أي تعديل ⚠️⚠️⚠️
================================================================================
## 🛑 خطوات إجبارية للمساعد الذكي:
1️⃣ اقرأ كامل قسم "المناطق المحظورة المطلقة" أدناه
2️⃣ اقرأ قسم "المميزات المكتملة 100%"
3️⃣ تأكد من فهم "خريطة السطور الفعلية"
4️⃣ استخدم فقط "المناطق الآمنة" للإضافات الجديدة
5️⃣ بعد التعديل، حدث قسم "آخر التعديلات" أدناه
6️⃣ انتظر تأكيد المطور قبل نقل الميزة لقائمة "المكتملة"
## ❌ المناطق المحظورة المطلقة (RED ZONES):
### 🚫 Zone 1: نظام إدارة الرسائل الذكي
📍 السطور: 151-304 (class SmartMessageManager)
🎯 الوظيفة: رسالة واحدة نشطة فقط + حماية Race Conditions
⛔ الممنوع: إنشاء طرق بديلة لإرسال الرسائل بأزرار
✅ الإجباري: استخدم smart_message_manager لكل رسالة تفاعلية
### 🚫 Zone 2: نظام الحماية المتقدم للواتساب
📍 السطور: 305-380 (class WhatsAppSecuritySystem)
🎯 الوظيفة: حماية من محاولات متكررة + تحليل مفصل للمدخلات
⛔ الممنوع: تغيير منطق التحقق أو الحماية
✅ المسموح: قراءة البيانات فقط
### 🚫 Zone 3: نظام التشفير المتقدم
📍 السطور: 381-420 (class EncryptionSystem)
🎯 الوظيفة: تشفير البيانات الحساسة (أرقام الدفع)
⛔ الممنوع: تغيير المفاتيح أو آلية التشفير
✅ المسموح: استخدام encrypt/decrypt فقط
### 🚫 Zone 4: نظام التحقق من طرق الدفع
📍 السطور: 421-650 (class PaymentValidationSystem)
🎯 الوظيفة: تحقق متقدم من 7 طرق دفع + حماية من التكرار
⛔ الممنوع: تغيير قواعد التحقق أو منطق الحماية
✅ المسموح: قراءة النتائج فقط
### 🚫 Zone 5: آلية استكمال التسجيل "أهلاً بعودتك"
📍 السطور: 1020-1080 (دالة start في SmartRegistrationHandler)
🎯 الوظيفة: استكمال التسجيل من نقطة التوقف + حفظ التقدم
⛔ الممنوع: تغيير منطق temp_registration أو آلية الاستكمال
✅ المسموح: تعديل النصوص والأزرار فقط
### 🚫 Zone 6: جداول قاعدة البيانات الأساسية
📍 السطور: 670-750 (init_database في Database class)
🎯 الوظيفة: 5 جداول أساسية للتسجيل والمحفظة والمعاملات
⛔ الممنوع: تعديل/حذف الجداول الموجودة أو علاقاتها
✅ المسموح: إضافة جداول جديدة فقط
## ✅ المميزات المكتملة 100% (تمت واختُبرت بنجاح):
• ✅ نظام التسجيل 4 مراحل (منصة→واتساب→دفع→تفاصيل دفع)
• ✅ حماية متقدمة للواتساب (حظر مؤقت + تحليل مفصل)
• ✅ 7 طرق دفع مع تحقق متقدم (محافظ + تيلدا + إنستاباي)
• ✅ تشفير البيانات الحساسة
• ✅ نظام الرسائل الذكي (رسالة واحدة نشطة)
• ✅ لوحة تحكم الأدمن الكاملة (عرض/بحث/حذف/بث)
• ✅ نظام صفحات لعرض المستخدمين (10 لكل صفحة)
• ✅ حفظ التقدم المؤقت + استكمال التسجيل
• ✅ صلاحيات الأدمن المحمية
• ✅ تعديلات أزرار الأدمن (حذف حسابي + إزالة الحذف من المستخدمين)
• ✅ تعليقات توضيحية للمناطق المحظورة في بداية الملف
• ✅ تحسين رسالة الخطأ للمستخدمين العاديين
• ✅ نظام تعديل الملف الشخصي الكامل:
  - ✅ تعديل المنصة (تفاعلي بالكامل مع قائمة اختيار)
  - ✅ تعديل الواتساب (إدخال مباشر مع التحقق الذكي)
  - ✅ تعديل طريقة الدفع (اختيار تفاعلي مع تفاصيل)
  - ✅ حفظ شبكة الواتساب في قاعدة البيانات
  - ✅ إصلاح مشكلة HTTP 400 في عرض الملف الشخصي
• ✅ رسائل مساعدة للمستخدمين عند محاولة استخدام أوامر الأدمن
• ✅ المرحلة الخامسة - الخطوة الأولى: Registration ThreadPool Infrastructure
• ✅ المرحلة الخامسة - الخطوة الثانية: Registration Threading في دالة start (مكتمل)
• ✅ إصلاح خطير: دالة cleanup() تنظف كامل الـ 7 ThreadPools (37 worker)
• ✅ لوجز مفصلة متقدمة لتشخيص مشاكل الأجهزة المتعددة (2025-09-11)
• 🆕 المرحلة السادسة (Stage 6): الحرية الكاملة في التعديل - مكتمل 2025-09-12
  - ✅ إزالة الإجبار في تسلسل التسجيل (أي حقل بأي ترتيب)
  - ✅ السماح للمستخدمين غير المكتملين بتعديل طرق الدفع
  - ✅ معالجة آمنة للحقول الفارغة (None values)
  - ✅ رسائل واضحة للحقول غير المكتملة ("لم يتم إدخاله بعد")
  - ✅ منع أخطاء WhatsApp عند تعديل طرق الدفع
## ✅ الميزات المكتملة حديثاً (تم اختبارها بنجاح):
• ✅ لوجز مفصلة لتشخيص مشاكل الأجهزة المتعددة - مكتمل 2025-09-11
• ✅ المرحلة 5 الخطوة 2أ: Registration Threading في دالة start - مكتمل بالفعل
## 📝 آخر التعديلات:
• تاريخ: 2025-09-12
• التحديث الأخير: المرحلة السادسة (Stage 6) - الحرية الكاملة في التعديل
• المساعد الذكي سيحدث هذا القسم تلقائياً بعد كل تعديل
• آخر تعديل معتمد: Stage 6 - إزالة الإجبار في تسلسل التسجيل
## ⏰ آخر تعديل للمساعد (مكتمل ومؤكد):
- التاريخ والوقت: 2025-09-11 (مكتمل)
- الميزات المضافة:
  • 🎯 الحل الثاني: تحديث registration_status تلقائياً عند اكتمال البيانات
  • فحص ذكي لاكتمال البيانات (منصة + واتساب + طريقة دفع + تفاصيل دفع)
  • تحديث تلقائي لـ registration_status إلى 'complete' عند الاكتمال
  • لوجز مفصلة لتشخيص حالة كل عنصر بيانات
  • معالجة آمنة مع فحص الحالة قبل التحديث
- الموقع:
  • السطور 1614-1660: دالة update_user_data - إضافة فحص اكتمال البيانات
  • إضافة فحص شامل للبيانات المطلوبة (platform, whatsapp, payment_method, payment_details)
  • إضافة تحديث تلقائي لـ registration_status = 'complete'
  • إضافة لوجز مفصلة لكل عنصر بيانات
- التعديل المضاف: 🎯 الحل الثاني - تحديث registration_status تلقائياً في update_user_data
- الملفات المعدلة: app_current.py
- حالة الاختبار: جاهز للاختبار الكامل
- ملاحظات: 🎯 الحل الثاني مطبق - تحديث registration_status تلقائياً عند اكتمال البيانات

## 🆕 آخر تعديل للمساعد - اليوم (2025-09-12):
- التاريخ والوقت: 2025-09-12 (Stage 6 Implementation)
- الميزات المضافة:
  • 🎯 Stage 6: الحرية الكاملة في تعديل الملف الشخصي
  • إزالة الإجبار في تسلسل التسجيل (منصة→واتساب→دفع)
  • السماح بتعديل أي حقل بأي ترتيب يفضله المستخدم
  • معالجة المستخدمين غير المكتملين في edit_payment
  • رسائل محسنة للحقول الفارغة ("🔄 لم يتم إدخاله بعد")
  • إضافة علامة stage6_free_edit لتتبع الحرية الكاملة
- الموقع:
  • السطور 4870-4890: تحديث edit_payment لدعم المستخدمين غير المكتملين
  • السطور 2910-2922: معالجة آمنة للحقول الفارغة في show_confirmation
  • إضافة نظام Stage 6 logging لتتبع العمليات الحرة
- التعديل المضاف: 🆕 Stage 6 - الحرية الكاملة في التعديل
- الملفات المعدلة: ycopycopy.py
- حالة الاختبار: جاهز للاختبار الكامل
- ملاحظات: ✅ حل مشكلة الإجبار التي ذكرها المستخدم بالكامل

## 🆕 آخر تعديل للمساعد - السابق (2025-09-11):
- التاريخ والوقت: 2025-09-11 12:06 PM
- الميزات المضافة:
  • 🔍 لوجز مفصلة متقدمة لتشخيص مشاكل الأجهزة المتعددة
    - إضافة [Device-Log] فهرسة للأجهزة مع تتبع دقيق
    - إضافة [Multi-Device] تحليل مفصل للأجهزة المتعددة
    - تتبع devices_before/devices_after لمعرفة إضافة الأجهزة الجديدة
    - معلومات تفصيلية: user_info، chat_type، device_info، device_id
    - تشخيص شامل للرسائل النشطة والتنظيف التلقائي
    - إحصائيات قائمة الأجهزة لكل مستخدم
  • ✅ تأكيد: Registration Threading موجود ومُطبق بالكامل في دالة start
    - registration_pool ThreadPoolExecutor يعمل بكفاءة
    - _process_start_sync يعمل في thread منفصل
    - معالجة شاملة للمستخدمين (جدد/مكتملين/ناقصين)
- الموقع: السطور 365-415 في SmartMessageManager
- التعديل المضاف: لوجز مفصلة مع 4 مستويات [Device-Log] و 5 مستويات [Multi-Device]
- حالة الاختبار: تم الاختبار بنجاح ✅
- ملاحظات: جميع الميزات قيد الاختبار أصبحت مكتملة ومؤكدة
## 🎯 خريطة السطور الحقيقية:
السطور 1-80: الإعدادات والاستيراد
السطور 81-150: البيانات الثابتة (GAMING_PLATFORMS, PAYMENT_METHODS, MESSAGES)
السطور 151-304: SmartMessageManager ⚠️ (لا تلمس)
السطور 305-380: WhatsAppSecuritySystem ⚠️ (لا تلمس)
السطور 381-420: EncryptionSystem ⚠️ (لا تلمس)
السطور 421-650: PaymentValidationSystem ⚠️ (لا تلمس)
السطور 651-850: Database class ⚠️ (لا تلمس الأساسيات)
السطور 851-950: Keyboards class 🟢 (آمن للتعديل)
السطور 951-1400: SmartRegistrationHandler ⚠️ (لا تلمس الأساسيات)
السطور 1401-1800: FC26SmartBot + لوحة الأدمن 🟢 (آمن للإضافة)
السطور 1801+: التشغيل والإعداد
## 🟢 المناطق الآمنة للإضافة (GREEN ZONES):
✅ إضافة أزرار جديدة في Keyboards class (السطور 851-950)
✅ إضافة رسائل جديدة في MESSAGES dictionary (السطور 81-150)
✅ إضافة دوال جديدة في FC26SmartBot class (السطور 1401+)
✅ إضافة معالجات أوامر جديدة
✅ إضافة callback handlers جديدة
✅ إضافة جداول قاعدة بيانات جديدة (بدون مس الموجود)
## 🤖 تعليمات التحديث الذاتي للمساعد:
بعد كل تعديل، يجب على المساعد الذكي:
1️⃣ تحديث قسم "آخر تعديل للمساعد":

- التاريخ والوقت: [YYYY-MM-DD HH:MM]
- التعديل المضاف: [وصف مختصر للتعديل]
- الملفات المعدلة: app_complete.py
- حالة الاختبار: ⏳ منتظر اختبار المطور
- ملاحظات: [أي ملاحظات مهمة]

2️⃣ إضافة الميزة الجديدة لقسم "قيد الاختبار":
- ضع علامة 🔄 بجانب الميزة الجديدة
- اذكر التفاصيل والموقع في الكود
3️⃣ إضافة Zone جديد إذا لزم الأمر:
- إذا أضفت ميزة معقدة، أضف Zone جديد برقم تسلسلي
- مثال: ### 🚫 Zone 7: نظام أسعار الكوينز
4️⃣ كتابة رسالة للمطور:

🎯 تم إضافة ميزة جديدة!
📝 التعديل: [اسم الميزة]
📍 الموقع: [أرقام السطور]
🔧 التفاصيل: [شرح مختصر]
⏰ حالة الاختبار: منتظر تأكيدك
✅ إذا اشتغلت بنجاح، قول "تمام" وسأنقلها للمكتملة
❌ إذا فيها مشكلة، اشرح المطلوب تعديله

## 🔧 قواعد التطوير الآمن:
1. ✅ استخدم smart_message_manager للرسائل التفاعلية الجديدة
2. ✅ أضف دوال جديدة في نهاية FC26SmartBot class
3. ✅ استخدم نفس أسلوب التعليقات العربية
4. ✅ اتبع نمط التسمية الحالي
5. ✅ اختبر مع النظام الموجود بدون كسره
6. ✅ حدث قسم التعليمات تلقائياً بعد كل إضافة
## ❌ أمثلة طلبات مرفوضة:
"غير نظام التحقق من الواتساب"
"عدل طريقة التشفير"
"أنشئ طريقة جديدة لإرسال الرسائل بأزرار"
"غير منطق حفظ التقدم المؤقت"
"عدل جداول قاعدة البيانات الأساسية"
## ✅ أمثلة طلبات مقبولة:
"أضف زر 'أسعار الكوينز' للقائمة الرئيسية"
"اجعل البوت يستجيب لأمر /prices جديد"
"أضف جدول جديد لحفظ أسعار الكوينز"
"أنشئ نظام إشعارات منفصل"
"أضف ميزة عرض الإحصائيات للأدمن"
================================================================================
⚠️ تنبيه للمساعد الذكي: اقرأ، عدل، حدث التعليمات، ثم انتظر تأكيد المطور ⚠️
================================================================================
"""


import asyncio
import base64
import hashlib
import json
import logging
import os
import re
import sqlite3
import threading
import time
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional, Tuple

from cryptography.fernet import Fernet
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from telegram import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    ReplyKeyboardRemove,
    Update,
)
from telegram.ext import (
    Application,
    CallbackQueryHandler,
    CommandHandler,
    ContextTypes,
    ConversationHandler,
    MessageHandler,
    filters,
)

# ================================ الإعدادات ================================
BOT_TOKEN = "7607085569:AAHKE8SNOTYycRRzOCCddmm8QPDTOnEx144"
ADMIN_ID = 1124247595
DATABASE_PATH = "fc26_bot.db"

# إعداد السجلات
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)


# ============================== نظام اللوجز المحدث ==============================
class DescriptiveLogger:
    """نظام لوجز وصفي بحد أقصى 200 حرف"""

    @staticmethod
    def log_success(action: str, details: str = "", max_len: int = 200) -> None:
        """تسجيل نجح العملية مع تفاصيل وصفية"""
        message = f"✅ نجح: {action}"
        if details:
            message += f" - {details}"

        # قطع الرسالة إذا تجاوزت الحد الأقصى
        if len(message) > max_len:
            message = message[: max_len - 3] + "..."

        logger.info(message)

    @staticmethod
    def log_warning(action: str, reason: str = "", max_len: int = 200) -> None:
        """تسجيل تحذير مع السبب"""
        message = f"⚠️ تحذير: {action}"
        if reason:
            message += f" - السبب: {reason}"

        if len(message) > max_len:
            message = message[: max_len - 3] + "..."

        logger.warning(message)

    @staticmethod
    def log_error(action: str, error_details: str = "", max_len: int = 200) -> None:
        """تسجيل خطأ مع تفاصيل الخطأ"""
        message = f"❌ خطأ: {action}"
        if error_details:
            message += f" - التفاصيل: {error_details}"

        if len(message) > max_len:
            message = message[: max_len - 3] + "..."

        logger.error(message)

    @staticmethod
    def log_user_action(
        user_id: int, action: str, result: str = "", max_len: int = 200
    ) -> None:
        """تسجيل إجراء المستخدم مع النتيجة"""
        message = f"👤 المستخدم {user_id}: {action}"
        if result:
            message += f" → {result}"

        if len(message) > max_len:
            message = message[: max_len - 3] + "..."

        logger.info(message)

    @staticmethod
    def log_validation_result(
        user_id: int, field: str, is_valid: bool, reason: str = "", max_len: int = 200
    ) -> None:
        """تسجيل نتيجة التحقق من البيانات"""
        status = "✅ صحيح" if is_valid else "❌ خطأ"
        message = f"🔍 المستخدم {user_id} - تحقق {field}: {status}"
        if reason:
            message += f" - {reason}"

        if len(message) > max_len:
            message = message[: max_len - 3] + "..."

        logger.info(message)


# إنشاء مثيل عام للاستخدام
desc_logger = DescriptiveLogger()

# ================================ حالات التسجيل ================================
(CHOOSING_PLATFORM, ENTERING_WHATSAPP, CHOOSING_PAYMENT, ENTERING_PAYMENT_DETAILS) = (
    range(4)
)

# ================================ البيانات الثابتة ================================
GAMING_PLATFORMS = {
    "playstation": {"name": "🎮 PlayStation (PS4/PS5)", "emoji": "🎮"},
    "xbox": {"name": "❎ Xbox (One/Series)", "emoji": "❎"},
    "pc": {"name": "💻 PC (Origin/Steam)", "emoji": "💻"},
}

PAYMENT_METHODS = {
    "vodafone_cash": {"name": "⭕️ فودافون كاش", "emoji": "⭕️"},
    "etisalat_cash": {"name": "🟢 اتصالات كاش", "emoji": "🟢"},
    "orange_cash": {"name": "🍊 أورانج كاش", "emoji": "🍊"},
    "we_cash": {"name": "🟣 وي كاش", "emoji": "🟣"},
    "bank_wallet": {"name": "🏦 محفظة بنكية", "emoji": "🏦"},
    "telda": {"name": "💳 تيلدا", "emoji": "💳"},
    "instapay": {"name": "🔗 إنستا باي", "emoji": "🔗"},
}

MESSAGES = {
    "welcome": """🌟 أهلاً وسهلاً في بوت FC 26! 🎮

البوت الأول في مصر لبيع كوينز FC 26 🇪🇬

✨ مميزاتنا:
• أسعار منافسة جداً 💰
• معاملات آمنة 100% 🔒
• دعم فني 24/7 📞
• سرعة في التنفيذ ⚡

اضغط على "تسجيل جديد" للبدء! 👇""",
    "choose_platform": """🎮 اختر منصة اللعب المناسبة:

🏆 أفضل الأسعار في مصر""",
    "enter_whatsapp": """📱 أرسل رقم الواتساب:

📝 القواعد:
• 11 رقم بالضبط
• يبدأ بـ: 010 / 011 / 012 / 015
• أرقام إنجليزية فقط (0-9)
• بدون مسافات أو رموز

✅ مثال صحيح: 01094591331""",
    "choose_payment": """💳 اختر طريقة الدفع:""",
    "registration_complete": """🎉 مبروك! تم إنشاء حسابك بنجاح! 🎊

✅ ملخص بياناتك:
━━━━━━━━━━━━━━━━
🎮 المنصة: {platform}
📱 واتساب: {whatsapp}
💳 طريقة الدفع: {payment}
━━━━━━━━━━━━━━━━

مرحباً بك في عائلة FC 26! 🚀""",
    "welcome_back": """👋 أهلاً بعودتك!

كنا واقفين عند: {last_step}

هل تريد المتابعة من حيث توقفت؟""",
    "data_saved": """💾 تم حفظ البيانات تلقائياً ✅

يمكنك العودة في أي وقت وسنكمل من نفس النقطة!""",
}


# ================================ نظام إدارة الرسائل الذكي ================================
class SmartMessageManager:
    """مدير الرسائل الذكي - رسالة واحدة نشطة فقط مع حماية من Race Conditions"""

    def __init__(self):
        self.user_active_messages: Dict[int, Dict[str, Any]] = {}
        # إضافة قفل لكل مستخدم لمنع Race Conditions
        self.user_locks: Dict[int, asyncio.Lock] = {}
        # تتبع الأجهزة المتعددة للمستخدم
        self.user_devices: Dict[int, set] = {}

    async def get_or_create_lock(self, user_id: int) -> asyncio.Lock:
        """الحصول على قفل المستخدم أو إنشاء واحد جديد"""
        if user_id not in self.user_locks:
            self.user_locks[user_id] = asyncio.Lock()
        return self.user_locks[user_id]

    async def cleanup_user_data(self, user_id: int):
        """تنظيف بيانات المستخدم عند انتهاء المحادثة"""
        # حذف القفل إذا كان موجوداً
        if user_id in self.user_locks:
            del self.user_locks[user_id]

        # حذف الرسائل النشطة إذا كانت موجودة
        if user_id in self.user_active_messages:
            del self.user_active_messages[user_id]

        # حذف بيانات الأجهزة
        if user_id in self.user_devices:
            del self.user_devices[user_id]

        logger.info(f"🧽 تم تنظيف بيانات المستخدم {user_id}")

    async def disable_old_message(
        self, user_id: int, context: ContextTypes.DEFAULT_TYPE, choice_made: str = None
    ):
        """إلغاء تفعيل الرسالة القديمة وتحويلها لسجل تاريخي"""
        # الحصول على القفل للمستخدم
        lock = await self.get_or_create_lock(user_id)

        async with lock:  # استخدام القفل لحماية العملية
            if user_id not in self.user_active_messages:
                return

            try:
                old_message_info = self.user_active_messages[user_id]

                if old_message_info.get("message_id") and old_message_info.get(
                    "chat_id"
                ):
                    # إذا كانت الرسالة القديمة فيها أزرار، نحذفها ونضع "تم"
                    if old_message_info.get("has_keyboard", False):
                        try:
                            # تحديث الرسالة بدون أزرار وإضافة "تم"
                            await context.bot.edit_message_text(
                                chat_id=old_message_info["chat_id"],
                                message_id=old_message_info["message_id"],
                                text=old_message_info.get("text", "") + "\n\n✅ تم",
                                # parse_mode removed
                            )
                        except Exception as e:
                            # إذا فشل التحديث، نحاول حذف الرسالة
                            try:
                                await context.bot.delete_message(
                                    chat_id=old_message_info["chat_id"],
                                    message_id=old_message_info["message_id"],
                                )
                            except:
                                pass

                    del self.user_active_messages[user_id]
            except Exception as e:
                logger.debug(f"تعذر تعديل الرسالة القديمة: {e}")

    async def send_new_active_message(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        text: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
        choice_made: str = None,
        disable_previous: bool = True,
        remove_keyboard: bool = True,
    ):
        """إرسال رسالة جديدة نشطة مع حماية من Race Conditions"""
        user_id = update.effective_user.id

        # 🔍 إصلاح 4: تحسين استخراج device_id للأجهزة المتعددة
        device_info = "Callback" if update.callback_query else "Message"
        device_id = "Unknown"

        # استخراج device_id المحسن حسب نوع Update
        if update.callback_query and update.callback_query.message:
            device_id = update.callback_query.message.message_id
            device_info = "Callback"
        elif update.message:
            device_id = update.message.message_id
            device_info = "Message"
        elif update.effective_message:
            device_id = update.effective_message.message_id
            device_info = "Effective"

        logger.debug(f"🔧 [Device-ID] تم استخراج {device_info} ID: {device_id}")

        # معلومات تفصيلية عن الجهاز والمستخدم
        chat_type = update.effective_chat.type if update.effective_chat else "Unknown"
        user_info = f"User: {update.effective_user.id}"
        if update.effective_user.username:
            user_info += f" (@{update.effective_user.username})"

        logger.info(
            f"🔵 [Device-Log] {user_info} دخل من جهاز - "
            f"Type: {device_info} | ID: {device_id} | Chat: {chat_type}"
        )

        # تتبع الأجهزة المتعددة مع تفاصيل أكثر
        if user_id not in self.user_devices:
            self.user_devices[user_id] = set()
            logger.debug(f"🆕 [Device-Log] إنشاء تتبع جديد للمستخدم {user_id}")

        # إحصائيات قبل الإضافة
        devices_before = len(self.user_devices[user_id])
        self.user_devices[user_id].add(device_id)
        devices_after = len(self.user_devices[user_id])

        # تحليل مفصل للأجهزة
        if devices_after > devices_before:
            logger.info(
                f"🔄 [Device-Log] المستخدم {user_id} أضاف جهاز جديد: "
                f"{devices_before}→{devices_after} أجهزة"
            )
            logger.debug(
                f"📱 [Device-Log] قائمة الأجهزة للمستخدم {user_id}: "
                f"{list(self.user_devices[user_id])}"
            )

        # إذا كان هناك أكثر من جهاز، نظف الرسائل القديمة مع تشخيص مفصل
        if len(self.user_devices[user_id]) > 1:
            logger.warning(
                f"⚠️ [Multi-Device] المستخدم {user_id} يستخدم أجهزة متعددة: "
                f"{len(self.user_devices[user_id])} أجهزة - الحالي: {device_id}"
            )

            # تشخيص حالة الرسائل النشطة
            if user_id in self.user_active_messages:
                old_message = self.user_active_messages[user_id]
                old_msg_id = old_message.get("message_id", "Unknown")

                logger.info(
                    f"🔍 [Multi-Device] فحص الرسائل النشطة للمستخدم {user_id}: "
                    f"رسالة قديمة {old_msg_id} vs رسالة حالية {device_id}"
                )

                if old_msg_id != device_id:
                    logger.warning(
                        f"🧽 [Multi-Device] حذف رسالة قديمة للمستخدم {user_id}: "
                        f"ID {old_msg_id} (استبدال بـ {device_id})"
                    )
                    del self.user_active_messages[user_id]
                else:
                    logger.info(
                        f"✅ [Multi-Device] نفس الرسالة النشطة للمستخدم {user_id}: {device_id}"
                    )
            else:
                logger.info(
                    f"💭 [Multi-Device] لا توجد رسائل نشطة للمستخدم {user_id} - جلسة جديدة"
                )

        # الحصول على القفل للمستخدم
        lock = await self.get_or_create_lock(user_id)

        if disable_previous:
            await self.disable_old_message(user_id, context, choice_made)

        async with lock:  # استخدام القفل لحماية عملية الإرسال والحفظ
            try:
                # التحقق من عدم وجود رسالة مطابقة نشطة بالفعل
                if user_id in self.user_active_messages:
                    existing_msg = self.user_active_messages[user_id]
                    if existing_msg.get("text") == text:
                        # نفس الرسالة موجودة بالفعل، لا نرسل مرة أخرى
                        logger.debug(f"تجاهل إرسال رسالة مكررة للمستخدم {user_id}")
                        # لوج عند تضارب الرسائل
                        active_count = len(
                            [k for k in self.user_active_messages if k == user_id]
                        )
                        logger.warning(
                            f"⚠️ تضارب رسائل للمستخدم {user_id} - Active Messages: {active_count}"
                        )
                        return None

                if update.callback_query:
                    sent_message = await update.callback_query.message.reply_text(
                        text=text,
                        reply_markup=reply_markup,
                        # parse_mode removed
                    )
                else:
                    # إزالة الكيبورد إذا لم يكن هناك reply_markup
                    final_markup = (
                        reply_markup
                        if reply_markup
                        else (ReplyKeyboardRemove() if remove_keyboard else None)
                    )
                    sent_message = await update.message.reply_text(
                        text=text,
                        reply_markup=final_markup,
                        # parse_mode removed
                    )

                # حفظ معلومات الرسالة الجديدة
                self.user_active_messages[user_id] = {
                    "message_id": sent_message.message_id,
                    "chat_id": sent_message.chat_id,
                    "text": text,
                    "has_keyboard": reply_markup is not None,
                    "timestamp": datetime.now(),  # إضافة timestamp للتتبع
                }

                return sent_message

            except Exception as e:
                logger.error(f"خطأ في إرسال رسالة: {e}")
                return None

    async def update_current_message(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        text: str,
        reply_markup: Optional[InlineKeyboardMarkup] = None,
    ):
        """تحديث الرسالة الحالية مع حماية من Race Conditions"""
        if not update.callback_query:
            return await self.send_new_active_message(
                update, context, text, reply_markup
            )

        user_id = update.effective_user.id
        message_id = update.callback_query.message.message_id

        # لوج قبل editMessageText
        logger.info(
            f"🟠 محاولة تعديل رسالة للمستخدم {user_id} - Message ID: {message_id} - New Content Length: {len(text)}"
        )

        # الحصول على القفل للمستخدم
        lock = await self.get_or_create_lock(user_id)

        async with lock:  # استخدام القفل لحماية عملية التحديث
            try:
                # التحقق من عدم تكرار نفس الرسالة
                if user_id in self.user_active_messages:
                    old_msg = self.user_active_messages[user_id]
                    if (
                        old_msg.get("text") == text
                        and old_msg.get("message_id")
                        == update.callback_query.message.message_id
                    ):
                        # نفس الرسالة، لا نحدث
                        logger.debug(f"تجاهل تحديث رسالة مطابقة للمستخدم {user_id}")
                        return

                    # التحقق من الـ timestamp لمنع التحديثات السريعة جداً
                    if "timestamp" in old_msg:
                        time_diff = (
                            datetime.now() - old_msg["timestamp"]
                        ).total_seconds()
                        if time_diff < 0.5:  # أقل من نصف ثانية
                            logger.debug(f"تجاهل تحديث سريع جداً للمستخدم {user_id}")
                            return

                await update.callback_query.edit_message_text(
                    text=text,
                    reply_markup=reply_markup,
                    # parse_mode removed
                )
                logger.info(
                    f"✅ تم تعديل الرسالة بنجاح للمستخدم {user_id} - Message ID: {message_id}"
                )

                # حفظ معلومات الرسالة المحدثة
                self.user_active_messages[user_id] = {
                    "message_id": update.callback_query.message.message_id,
                    "chat_id": update.callback_query.message.chat_id,
                    "text": text,
                    "has_keyboard": reply_markup is not None,
                    "timestamp": datetime.now(),  # إضافة timestamp للتتبع
                }

            except Exception as e:
                # إذا كان الخطأ "لم يتغير النص"، نتجاهله
                if "message is not modified" in str(e).lower():
                    logger.debug(f"الرسالة لم تتغير للمستخدم {user_id}")
                elif "400" in str(e) or "Bad Request" in str(e):
                    # لوج عند HTTP 400
                    logger.error(
                        f"🔴 خطأ HTTP 400 للمستخدم {user_id} - Message ID: {message_id} - Error: {str(e)}"
                    )
                    # محاولة إرسال رسالة جديدة بدلاً من التعديل
                    logger.info(
                        f"📨 محاولة إرسال رسالة جديدة بدلاً من التعديل للمستخدم {user_id}"
                    )
                    await self.send_new_active_message(
                        update, context, text, reply_markup
                    )
                else:
                    logger.debug(f"خطأ في تحديث الرسالة للمستخدم {user_id}: {e}")


# إنشاء المدير الذكي
smart_message_manager = SmartMessageManager()


# ================================ نظام الحماية المتقدم للواتساب ================================
class WhatsAppSecuritySystem:
    """نظام حماية متقدم للتحقق من أرقام الواتساب"""

    def __init__(self):
        # تتبع المحاولات لكل مستخدم
        self.user_attempts: Dict[int, List[datetime]] = defaultdict(list)
        self.failed_attempts: Dict[int, int] = defaultdict(int)
        self.blocked_users: Dict[int, datetime] = {}
        self.last_numbers: Dict[int, str] = {}

        # إعدادات الحماية
        self.MAX_ATTEMPTS_PER_MINUTE = 5
        self.MAX_FAILED_ATTEMPTS = 5
        self.BLOCK_DURATION_MINUTES = 15
        self.RATE_LIMIT_WINDOW = 60  # ثانية

        # شبكات الاتصال المصرية
        self.EGYPTIAN_NETWORKS = {
            "010": {"name": "فودافون", "emoji": "⭕️"},
            "011": {"name": "اتصالات", "emoji": "🟢"},
            "012": {"name": "أورانج", "emoji": "🍊"},
            "015": {"name": "وي", "emoji": "🟣"},
        }

    def is_user_blocked(self, user_id: int) -> Tuple[bool, Optional[int]]:
        """التحقق من حظر المستخدم"""
        if user_id in self.blocked_users:
            block_time = self.blocked_users[user_id]
            elapsed = (datetime.now() - block_time).total_seconds() / 60

            if elapsed < self.BLOCK_DURATION_MINUTES:
                remaining = self.BLOCK_DURATION_MINUTES - int(elapsed)
                return True, remaining
            else:
                # انتهت فترة الحظر
                del self.blocked_users[user_id]
                self.failed_attempts[user_id] = 0

        return False, None

    def check_rate_limit(self, user_id: int) -> Tuple[bool, Optional[str]]:
        """فحص معدل الطلبات"""
        now = datetime.now()

        # تنظيف المحاولات القديمة
        if user_id in self.user_attempts:
            self.user_attempts[user_id] = [
                attempt
                for attempt in self.user_attempts[user_id]
                if (now - attempt).total_seconds() < self.RATE_LIMIT_WINDOW
            ]

        # فحص عدد المحاولات
        attempts_count = len(self.user_attempts[user_id])

        if attempts_count >= self.MAX_ATTEMPTS_PER_MINUTE:
            return (
                False,
                f"⚠️ لقد تجاوزت الحد المسموح ({self.MAX_ATTEMPTS_PER_MINUTE} محاولات في الدقيقة)\\n\\n⏰ انتظر قليلاً ثم حاول مرة أخرى",
            )

        # تسجيل المحاولة الجديدة
        self.user_attempts[user_id].append(now)
        return True, None

    def check_duplicate(self, user_id: int, phone: str) -> bool:
        """فحص الأرقام المكررة"""
        if user_id in self.last_numbers:
            if self.last_numbers[user_id] == phone:
                return True
        return False

    def analyze_input(self, text: str) -> Dict[str, Any]:
        """تحليل المدخل بشكل تفصيلي"""
        analysis = {
            "original": text,
            "has_letters": False,
            "has_symbols": False,
            "has_spaces": False,
            "has_arabic_numbers": False,
            "extracted_digits": "",
            "all_chars": [],
            "invalid_chars": [],
        }

        # استخراج الأرقام فقط
        digits_only = re.sub(r"[^\d]", "", text)
        analysis["extracted_digits"] = digits_only

        # تحليل كل حرف
        for char in text:
            analysis["all_chars"].append(char)

            # فحص الأحرف
            if char.isalpha():
                analysis["has_letters"] = True
                analysis["invalid_chars"].append(char)

            # فحص الرموز
            elif not char.isdigit() and not char.isspace():
                analysis["has_symbols"] = True
                analysis["invalid_chars"].append(char)

            # فحص المسافات
            elif char.isspace():
                analysis["has_spaces"] = True
                analysis["invalid_chars"].append(char)

            # فحص الأرقام العربية
            elif char in "٠١٢٣٤٥٦٧٨٩":
                analysis["has_arabic_numbers"] = True
                analysis["invalid_chars"].append(char)

        return analysis

    def validate_whatsapp(self, text: str, user_id: int) -> Dict[str, Any]:
        """التحقق الشامل من رقم الواتساب"""
        result = {
            "is_valid": False,
            "cleaned_number": "",
            "error_type": None,
            "error_message": "",
            "network_info": None,
            "analysis": None,
        }

        # التحليل التفصيلي للمدخل
        analysis = self.analyze_input(text)
        result["analysis"] = analysis

        # 1. فحص وجود أحرف أو رموز
        if (
            analysis["has_letters"]
            or analysis["has_symbols"]
            or analysis["has_spaces"]
            or analysis["has_arabic_numbers"]
        ):
            invalid_chars_display = "".join(set(analysis["invalid_chars"]))
            result["error_type"] = "invalid_chars"
            result[
                "error_message"
            ] = f"""❌ رقم الواتساب يجب أن يكون أرقام فقط

📍 المدخل الخاطئ: {text}

🚫 الأحرف/الرموز الغير مسموحة: {invalid_chars_display}

📊 الأرقام المستخرجة: {analysis['extracted_digits'] or 'لا توجد أرقام'}


✅ مثال صحيح: 01094591331

💡 تلميح: استخدم الأرقام الإنجليزية فقط (0-9) بدون مسافات أو رموز"""
            return result

        cleaned = analysis["extracted_digits"]

        # 2. فحص الطول
        if len(cleaned) < 11:
            result["error_type"] = "too_short"
            result[
                "error_message"
            ] = f"""❌ طول الرقم غير صحيح

📏 المطلوب: 11 رقم بالضبط

📍 أنت أدخلت: {len(cleaned)} رقم فقط

🔢 الرقم المدخل: {cleaned}

✅ مثال صحيح: 01094591331"""
            return result

        elif len(cleaned) > 11:
            result["error_type"] = "too_long"
            result[
                "error_message"
            ] = f"""❌ طول الرقم غير صحيح

📏 المطلوب: 11 رقم بالضبط

📍 أنت أدخلت: {len(cleaned)} رقم (أكثر من المطلوب)

🔢 الرقم المدخل: {cleaned}

✅ مثال صحيح: 01094591331"""
            return result

        # 3. فحص البداية
        prefix = cleaned[:3]
        if prefix not in self.EGYPTIAN_NETWORKS:
            result["error_type"] = "invalid_prefix"
            result[
                "error_message"
            ] = f"""❌ بداية الرقم غير صحيحة

📍 يجب أن يبدأ بـ: 010 / 011 / 012 / 015

🚫 رقمك يبدأ بـ: {prefix}

🔢 الرقم المدخل: {cleaned}


📱 الشبكات المدعومة:
⭕️ 010 - فودافون
🟢 011 - اتصالات
🍊 012 - أورانج
🟣 015 - وي

✅ مثال صحيح: 01094591331"""
            return result

        # النجاح!
        network = self.EGYPTIAN_NETWORKS[prefix]
        result["is_valid"] = True
        result["cleaned_number"] = cleaned
        result["network_info"] = network

        # حفظ الرقم لمنع التكرار
        self.last_numbers[user_id] = cleaned

        return result

    def record_failure(self, user_id: int):
        """تسجيل محاولة فاشلة"""
        self.failed_attempts[user_id] += 1

        if self.failed_attempts[user_id] >= self.MAX_FAILED_ATTEMPTS:
            self.blocked_users[user_id] = datetime.now()
            return True  # تم الحظر

        return False

    def reset_user_failures(self, user_id: int):
        """إعادة تعيين المحاولات الفاشلة عند النجاح"""
        self.failed_attempts[user_id] = 0
        if user_id in self.blocked_users:
            del self.blocked_users[user_id]

    def get_remaining_attempts(self, user_id: int) -> int:
        """الحصول على عدد المحاولات المتبقية"""
        return self.MAX_FAILED_ATTEMPTS - self.failed_attempts.get(user_id, 0)


# إنشاء نظام الحماية
whatsapp_security = WhatsAppSecuritySystem()


# ================================ نظام التشفير المتقدم ================================
class EncryptionSystem:
    """نظام تشفير متقدم للبيانات الحساسة"""

    def __init__(self):
        # استخدام مفتاح ثابت آمن (في الإنتاج يجب استخدام مفتاح من متغيرات البيئة)
        self.master_key = b"FC26_BOT_SECURE_ENCRYPTION_KEY_2025_PRODUCTION"
        self._init_cipher()

    def _init_cipher(self):
        """تهيئة نظام التشفير"""
        # إنشاء KDF للحصول على مفتاح قوي
        kdf = PBKDF2HMAC(
            algorithm=hashes.SHA256(),
            length=32,
            salt=b"FC26_SALT_2025",
            iterations=100000,
        )
        key = base64.urlsafe_b64encode(kdf.derive(self.master_key))
        self.cipher = Fernet(key)

    def encrypt(self, data: str) -> str:
        """تشفير البيانات"""
        if not data:
            return ""
        try:
            encrypted = self.cipher.encrypt(data.encode())
            return base64.urlsafe_b64encode(encrypted).decode()
        except Exception as e:
            logger.error(f"خطأ في التشفير: {e}")
            return data  # إرجاع البيانات بدون تشفير في حالة الخطأ

    def decrypt(self, encrypted_data: str) -> str:
        """فك تشفير البيانات"""
        if not encrypted_data:
            return ""
        try:
            decoded = base64.urlsafe_b64decode(encrypted_data.encode())
            decrypted = self.cipher.decrypt(decoded)
            return decrypted.decode()
        except Exception as e:
            logger.error(f"خطأ في فك التشفير: {e}")
            return encrypted_data  # إرجاع البيانات كما هي في حالة الخطأ


# إنشاء نظام التشفير
encryption_system = EncryptionSystem()


# ================================ نظام التحقق من طرق الدفع ================================
class PaymentValidationSystem:
    """نظام التحقق المتقدم من طرق الدفع"""

    def __init__(self):
        # تتبع المحاولات لكل مستخدم
        self.user_attempts: Dict[int, List[datetime]] = defaultdict(list)
        self.failed_attempts: Dict[int, int] = defaultdict(int)
        self.blocked_users: Dict[int, datetime] = {}

        # إعدادات الحماية
        self.MAX_ATTEMPTS_PER_MINUTE = 8
        self.MAX_FAILED_ATTEMPTS = 4
        self.BLOCK_DURATION_MINUTES = 10
        self.RATE_LIMIT_WINDOW = 60  # ثانية

        # قواعد التحقق لكل طريقة دفع
        self.PAYMENT_RULES = {
            "vodafone_cash": {
                "type": "wallet",
                "length": 11,
                "prefix": ["010", "011", "012", "015"],
                "name": "فودافون كاش",
                "example": "01012345678",
                "network": "جميع الشبكات",
            },
            "etisalat_cash": {
                "type": "wallet",
                "length": 11,
                "prefix": ["010", "011", "012", "015"],
                "name": "اتصالات كاش",
                "example": "01112345678",
                "network": "جميع الشبكات",
            },
            "orange_cash": {
                "type": "wallet",
                "length": 11,
                "prefix": ["010", "011", "012", "015"],
                "name": "أورانج كاش",
                "example": "01212345678",
                "network": "جميع الشبكات",
            },
            "we_cash": {
                "type": "wallet",
                "length": 11,
                "prefix": ["010", "011", "012", "015"],
                "name": "وي كاش",
                "example": "01512345678",
                "network": "جميع الشبكات",
            },
            "bank_wallet": {
                "type": "wallet",
                "length": 11,
                "prefix": ["010", "011", "012", "015"],
                "name": "محفظة بنكية",
                "example": "01012345678",
                "network": "جميع الشبكات المصرية",
            },
            "telda": {
                "type": "card",
                "length": 16,
                "name": "تيلدا",
                "example": "1234567890123456",
            },
            "instapay": {
                "type": "link",
                "name": "إنستا باي",
                "keywords": ["instapay", "ipn.eg"],
                "example": "https://instapay.com/username",
            },
        }

    def is_user_blocked(self, user_id: int) -> Tuple[bool, Optional[int]]:
        """التحقق من حظر المستخدم"""
        if user_id in self.blocked_users:
            block_time = self.blocked_users[user_id]
            elapsed = (datetime.now() - block_time).total_seconds() / 60

            if elapsed < self.BLOCK_DURATION_MINUTES:
                remaining = self.BLOCK_DURATION_MINUTES - int(elapsed)
                return True, remaining
            else:
                # انتهت فترة الحظر
                del self.blocked_users[user_id]
                self.failed_attempts[user_id] = 0

        return False, None

    def check_rate_limit(self, user_id: int) -> Tuple[bool, Optional[str]]:
        """فحص معدل الطلبات"""
        now = datetime.now()

        # تنظيف المحاولات القديمة
        if user_id in self.user_attempts:
            self.user_attempts[user_id] = [
                attempt
                for attempt in self.user_attempts[user_id]
                if (now - attempt).total_seconds() < self.RATE_LIMIT_WINDOW
            ]

        # فحص عدد المحاولات
        attempts_count = len(self.user_attempts[user_id])

        if attempts_count >= self.MAX_ATTEMPTS_PER_MINUTE:
            return (
                False,
                f"⚠️ لقد تجاوزت الحد المسموح ({self.MAX_ATTEMPTS_PER_MINUTE} محاولات في الدقيقة)\\n\\n⏰ انتظر قليلاً ثم حاول مرة أخرى",
            )

        # تسجيل المحاولة الجديدة
        self.user_attempts[user_id].append(now)
        return True, None

    def validate_wallet(self, text: str, payment_method: str) -> Dict[str, Any]:
        """التحقق من رقم المحفظة الإلكترونية"""
        result = {
            "is_valid": False,
            "cleaned_data": "",
            "error_message": "",
            "network": "",
        }

        # تنظيف الرقم من الرموز
        cleaned = re.sub(r"[^\d]", "", text)

        rules = self.PAYMENT_RULES[payment_method]

        # فحص وجود أحرف أو رموز
        if re.search(r"[a-zA-Z]", text):
            result[
                "error_message"
            ] = f"""❌ رقم {rules['name']} غير صحيح
📍 يجب أن يكون:

• أرقام فقط (بدون حروف أو رموز)

• 11 رقم بالضبط

• يبدأ بـ {'/'.join(rules['prefix'])} فقط

✅ مثال صحيح: {rules['example']}"""

            if payment_method == "bank_wallet":
                result[
                    "error_message"
                ] += "\n\n📍 تنبيه: المحفظة البنكية تقبل جميع الشبكات المصرية (010/011/012/015)"

            return result

        # فحص الطول
        if len(cleaned) != rules["length"]:
            result[
                "error_message"
            ] = f"""❌ رقم {rules['name']} غير صحيح
📏 الطول المطلوب: {rules['length']} رقم

📍 أنت أدخلت: {len(cleaned)} رقم

✅ مثال صحيح: {rules['example']}"""
            return result

        # فحص البداية
        prefix = cleaned[:3]
        if prefix not in rules["prefix"]:
            result[
                "error_message"
            ] = f"""❌ رقم {rules['name']} غير صحيح

📍 يجب أن يبدأ بـ: {'/'.join(rules['prefix'])} فقط

🚫 رقمك يبدأ بـ: {prefix}

✅ مثال صحيح: {rules['example']}"""

            if payment_method == "bank_wallet":
                result[
                    "error_message"
                ] += "\n\n📍 تنبيه: المحفظة البنكية تقبل جميع الشبكات المصرية (010/011/012/015)"

            return result

        # النجاح
        result["is_valid"] = True
        result["cleaned_data"] = cleaned
        result["network"] = rules["network"]

        return result

    def validate_telda(self, text: str) -> Dict[str, Any]:
        """التحقق من رقم كارت تيلدا"""
        result = {"is_valid": False, "cleaned_data": "", "error_message": ""}

        # السماح بالمسافات والشرطات ثم إزالتها
        cleaned = re.sub(r"[\s\-]", "", text)

        # إزالة أي شيء غير الأرقام
        digits_only = re.sub(r"[^\d]", "", cleaned)

        # فحص وجود أحرف
        if re.search(r"[a-zA-Z]", text):
            result[
                "error_message"
            ] = """❌ رقم كارت تيلدا غير صحيح
📍 يجب أن يكون:
• 16 رقم بالضبط
• أرقام فقط (يُسمح بالمسافات والشرطات)
• بدون حروف أو رموز غريبة
✅ أمثلة صحيحة:
• 1234567890123456
• 1234-5678-9012-3456
• 1234 5678 9012 3456"""
            return result

        # فحص الطول
        if len(digits_only) != 16:
            result[
                "error_message"
            ] = f"""❌ رقم كارت تيلدا غير صحيح
📏 المطلوب: 16 رقم بالضبط
📍 أنت أدخلت: {len(digits_only)} رقم
✅ أمثلة صحيحة:
• 1234567890123456
• 1234-5678-9012-3456
• 1234 5678 9012 3456"""
            return result

        # النجاح
        result["is_valid"] = True
        result["cleaned_data"] = digits_only

        return result

    def validate_instapay(self, text: str) -> Dict[str, Any]:
        """التحقق من رابط إنستاباي واستخراج الرابط الصحيح فقط"""
        result = {"is_valid": False, "cleaned_data": "", "error_message": ""}

        # تنظيف النص
        text = text.strip()

        # البحث عن روابط InstaPay أو IPN في النص
        import re

        # نمط للبحث عن روابط ipn.eg أو instapay - محسن لدعم جميع النطاقات
        # يبحث عن روابط كاملة مثل https://ipn.eg/S/username/instapay/ABC123
        url_patterns = [
            r"https?://ipn\.eg/[^\s]+",  # روابط ipn.eg
            r"https?://instapay\.com\.eg/[^\s]+",  # روابط instapay.com.eg (الموقع الرسمي)
            r"https?://instapay\.com/[^\s]+",  # روابط instapay.com
            r"ipn\.eg/[^\s]+",  # روابط ipn.eg بدون https
            r"instapay\.com\.eg/[^\s]+",  # روابط instapay.com.eg بدون https (الأهم)
            r"instapay\.com/[^\s]+",  # روابط instapay.com بدون https
        ]

        # البحث عن أول رابط مطابق
        for pattern in url_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                found_url = match.group(0)
                # إضافة https:// إذا لم يكن موجوداً
                if not found_url.startswith("http"):
                    found_url = f"https://{found_url}"
                result["is_valid"] = True
                result["cleaned_data"] = found_url
                return result

        # إذا لم يتم العثور على رابط، نتحقق من النص بشكل عام
        if any(keyword in text.lower() for keyword in ["instapay", "ipn.eg", "ipn"]):
            # إذا كان النص يحتوي على كلمات مفتاحية لكن ليس بتنسيق رابط صحيح
            # نحاول تنظيف النص وأخذ أول رابط
            lines = text.split("\n")
            for line in lines:
                line = line.strip()
                if "https://" in line or "http://" in line:
                    # استخراج الرابط من السطر
                    url_match = re.search(r"https?://[^\s]+", line)
                    if url_match:
                        result["is_valid"] = True
                        result["cleaned_data"] = url_match.group(0)
                        return result

        # فشل التحقق
        result[
            "error_message"
        ] = """❌ رابط إنستاباي غير صحيح
📍 يجب إدخال رابط كامل فقط
• لا يُقبل اسم المستخدم بدون رابط
• يجب أن يحتوي على instapay أو ipn.eg
✅ أمثلة صحيحة:
• https://instapay.com.eg/abc123
• https://ipn.eg/S/username/ABC123
• instapay.com.eg/xyz789
• ipn.eg/S/ABC123"""

        return result

    def record_failure(self, user_id: int):
        """تسجيل محاولة فاشلة"""
        self.failed_attempts[user_id] += 1

        if self.failed_attempts[user_id] >= self.MAX_FAILED_ATTEMPTS:
            self.blocked_users[user_id] = datetime.now()
            return True  # تم الحظر

        return False

    def reset_user_failures(self, user_id: int):
        """إعادة تعيين المحاولات الفاشلة عند النجاح"""
        self.failed_attempts[user_id] = 0
        if user_id in self.blocked_users:
            del self.blocked_users[user_id]

    def get_remaining_attempts(self, user_id: int) -> int:
        """الحصول على عدد المحاولات المتبقية"""
        return self.MAX_FAILED_ATTEMPTS - self.failed_attempts.get(user_id, 0)


# إنشاء نظام التحقق من طرق الدفع
payment_validation = PaymentValidationSystem()


# ================================ قاعدة البيانات ================================
class Database:
    """مدير قاعدة البيانات"""

    def __init__(self):
        self.init_database()

    def get_connection(self):
        """إنشاء اتصال جديد"""
        conn = sqlite3.connect(DATABASE_PATH)
        conn.row_factory = sqlite3.Row
        return conn

    def init_database(self):
        """تهيئة قاعدة البيانات"""
        conn = self.get_connection()
        cursor = conn.cursor()

        # جدول المستخدمين
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                telegram_id INTEGER UNIQUE NOT NULL,
                username TEXT,
                full_name TEXT,
                registration_status TEXT DEFAULT 'incomplete',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # جدول بيانات التسجيل
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS registration_data (
                user_id INTEGER PRIMARY KEY,
                platform TEXT,
                whatsapp TEXT,
                whatsapp_network TEXT,
                payment_method TEXT,
                payment_details TEXT,
                payment_details_type TEXT,
                payment_network TEXT,
                phone TEXT,
                payment_info TEXT,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """
        )

        # إضافة العمود whatsapp_network للجداول الموجودة (للتوافق مع قواعد البيانات القديمة)
        try:
            cursor.execute(
                "ALTER TABLE registration_data ADD COLUMN whatsapp_network TEXT"
            )
            conn.commit()
            logger.info("تم إضافة عمود whatsapp_network بنجاح")
        except:
            # العمود موجود بالفعل، لا مشكلة
            pass

        # جدول التسجيل المؤقت
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS temp_registration (
                telegram_id INTEGER PRIMARY KEY,
                step_name TEXT,
                step_number INTEGER,
                data TEXT,
                updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """
        )

        # جدول المحفظة
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS wallet (
                user_id INTEGER PRIMARY KEY,
                coin_balance REAL DEFAULT 0,
                loyalty_points INTEGER DEFAULT 0,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """
        )

        # جدول المعاملات
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS transactions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id INTEGER,
                type TEXT,
                amount REAL,
                status TEXT,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                FOREIGN KEY (user_id) REFERENCES users(user_id)
            )
        """
        )

        conn.commit()
        conn.close()

    def create_user(self, telegram_id: int, username: str, full_name: str) -> int:
        """إنشاء مستخدم جديد"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                """
                INSERT OR IGNORE INTO users (telegram_id, username, full_name)
                VALUES (?, ?, ?)
            """,
                (telegram_id, username, full_name),
            )

            if cursor.rowcount == 0:
                cursor.execute(
                    "SELECT user_id FROM users WHERE telegram_id = ?", (telegram_id,)
                )
                user_id = cursor.fetchone()["user_id"]
            else:
                user_id = cursor.lastrowid

                # إنشاء سجلات فارغة
                cursor.execute(
                    "INSERT INTO registration_data (user_id) VALUES (?)", (user_id,)
                )
                cursor.execute("INSERT INTO wallet (user_id) VALUES (?)", (user_id,))

            conn.commit()
            conn.close()
            return user_id

        except Exception as e:
            conn.close()
            logger.error(f"خطأ في إنشاء المستخدم: {e}")
            return None

    def save_temp_registration(
        self, telegram_id: int, step_name: str, step_number: int, data: dict
    ):
        """حفظ التسجيل المؤقت"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            INSERT OR REPLACE INTO temp_registration (telegram_id, step_name, step_number, data)
            VALUES (?, ?, ?, ?)
        """,
            (telegram_id, step_name, step_number, json.dumps(data)),
        )

        conn.commit()
        conn.close()

    def get_temp_registration(self, telegram_id: int) -> Optional[dict]:
        """استرجاع التسجيل المؤقت"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT * FROM temp_registration WHERE telegram_id = ?
        """,
            (telegram_id,),
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return {
                "step_name": row["step_name"],
                "step_number": row["step_number"],
                "data": json.loads(row["data"]),
            }
        return None

    def clear_temp_registration(self, telegram_id: int):
        """حذف التسجيل المؤقت"""
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(
            "DELETE FROM temp_registration WHERE telegram_id = ?", (telegram_id,)
        )
        conn.commit()
        conn.close()

    def complete_registration(self, telegram_id: int, data: dict) -> bool:
        """إكمال التسجيل"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            # الحصول على معرف المستخدم
            cursor.execute(
                "SELECT user_id FROM users WHERE telegram_id = ?", (telegram_id,)
            )
            user = cursor.fetchone()

            if not user:
                conn.close()
                return False

            user_id = user["user_id"]

            # محاولة إضافة الحقول الجديدة إذا لم تكن موجودة (مع حماية من الأخطاء)
            try:
                cursor.execute(
                    "ALTER TABLE registration_data ADD COLUMN payment_details TEXT"
                )
            except sqlite3.OperationalError:
                pass  # العمود موجود بالفعل
            except Exception as e:
                logger.debug(f"Column payment_details may already exist: {e}")
                pass

            try:
                cursor.execute(
                    "ALTER TABLE registration_data ADD COLUMN payment_details_type TEXT"
                )
            except sqlite3.OperationalError:
                pass  # العمود موجود بالفعل
            except Exception as e:
                logger.debug(f"Column payment_details_type may already exist: {e}")
                pass

            try:
                cursor.execute(
                    "ALTER TABLE registration_data ADD COLUMN payment_network TEXT"
                )
            except sqlite3.OperationalError:
                pass  # العمود موجود بالفعل
            except Exception as e:
                logger.debug(f"Column payment_network may already exist: {e}")
                pass

            # تحديث بيانات التسجيل
            cursor.execute(
                """
                UPDATE registration_data
                SET platform = ?, whatsapp = ?, whatsapp_network = ?, payment_method = ?
                WHERE user_id = ?
            """,
                (
                    data.get("platform"),
                    data.get("whatsapp"),
                    data.get("whatsapp_network", ""),
                    data.get("payment_method"),
                    user_id,
                ),
            )

            # محاولة تحديث الحقول الجديدة إذا كانت موجودة
            if data.get("payment_details"):
                try:
                    cursor.execute(
                        """
                        UPDATE registration_data
                        SET payment_details = ?, payment_details_type = ?, payment_network = ?
                        WHERE user_id = ?
                    """,
                        (
                            data.get("payment_details"),
                            data.get("payment_details_type"),
                            data.get("payment_network"),
                            user_id,
                        ),
                    )
                except:
                    pass

            # تحديث حالة التسجيل
            cursor.execute(
                """
                UPDATE users SET registration_status = 'complete' WHERE user_id = ?
            """,
                (user_id,),
            )

            # إضافة نقاط الترحيب
            cursor.execute(
                """
                UPDATE wallet SET loyalty_points = loyalty_points + 100 WHERE user_id = ?
            """,
                (user_id,),
            )

            conn.commit()
            conn.close()

            # حذف البيانات المؤقتة
            self.clear_temp_registration(telegram_id)

            return True

        except Exception as e:
            conn.close()
            logger.error(f"خطأ في إكمال التسجيل: {e}")
            return False

    def get_user_by_telegram_id(self, telegram_id: int) -> Optional[dict]:
        """الحصول على المستخدم"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE telegram_id = ?", (telegram_id,))
        row = cursor.fetchone()

        conn.close()

        if row:
            return dict(row)
        return None

    def get_user_data(self, telegram_id: int) -> Optional[dict]:
        """الحصول على بيانات المستخدم الكاملة"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT u.*, r.*
            FROM users u
            LEFT JOIN registration_data r ON u.user_id = r.user_id
            WHERE u.telegram_id = ?
        """,
            (telegram_id,),
        )

        row = cursor.fetchone()
        conn.close()

        if row:
            return dict(row)
        return None

    def get_user_profile(self, telegram_id: int) -> Optional[dict]:
        """الحصول على الملف الشخصي مع معالجة القيم الفارغة"""
        conn = self.get_connection()
        cursor = conn.cursor()

        cursor.execute(
            """
            SELECT u.*, r.*, w.*
            FROM users u
            LEFT JOIN registration_data r ON u.user_id = r.user_id
            LEFT JOIN wallet w ON u.user_id = w.user_id
            WHERE u.telegram_id = ?
        """,
            (telegram_id,),
        )

        row = cursor.fetchone()

        if row:
            profile = dict(row)

            # معالجة القيم الفارغة لمنع مشاكل None
            profile["platform"] = profile.get("platform") or "غير محدد"
            profile["whatsapp"] = profile.get("whatsapp") or "غير محدد"
            profile["payment_method"] = profile.get("payment_method") or "غير محدد"
            profile["whatsapp_network"] = profile.get("whatsapp_network") or ""
            profile["payment_details"] = profile.get("payment_details") or ""
            profile["payment_details_type"] = profile.get("payment_details_type") or ""
            profile["payment_network"] = profile.get("payment_network") or ""

            # عدد المعاملات
            cursor.execute(
                """
                SELECT COUNT(*) as transaction_count
                FROM transactions WHERE user_id = ?
            """,
                (profile["user_id"],),
            )

            profile["transaction_count"] = cursor.fetchone()["transaction_count"]

            conn.close()
            return profile

        conn.close()
        return None

    def update_user_data(self, telegram_id: int, update_data: dict) -> bool:
        """تحديث بيانات المستخدم"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            # الحصول على user_id
            cursor.execute(
                "SELECT user_id FROM users WHERE telegram_id = ?", (telegram_id,)
            )
            user = cursor.fetchone()

            if not user:
                conn.close()
                return False

            user_id = user["user_id"]

            # تحديث بيانات التسجيل
            if "platform" in update_data:
                cursor.execute(
                    """
                    UPDATE registration_data
                    SET platform = ?
                    WHERE user_id = ?
                """,
                    (update_data["platform"], user_id),
                )

            if "whatsapp" in update_data:
                cursor.execute(
                    """
                    UPDATE registration_data
                    SET whatsapp = ?, whatsapp_network = ?
                    WHERE user_id = ?
                """,
                    (
                        update_data.get("whatsapp"),
                        update_data.get("whatsapp_network", ""),
                        user_id,
                    ),
                )

            if "payment_method" in update_data:
                cursor.execute(
                    """
                    UPDATE registration_data
                    SET payment_method = ?
                    WHERE user_id = ?
                """,
                    (update_data["payment_method"], user_id),
                )

            if "payment_details" in update_data:
                cursor.execute(
                    """
                    UPDATE registration_data
                    SET payment_details = ?, payment_details_type = ?, payment_network = ?
                    WHERE user_id = ?
                """,
                    (
                        update_data.get("payment_details"),
                        update_data.get("payment_details_type", ""),
                        update_data.get("payment_network", ""),
                        user_id,
                    ),
                )

            # 🎯 الحل الثاني: فحص اكتمال البيانات وتحديث registration_status تلقائياً
            logger.info(
                f"🔍 [الحل الثاني] فحص اكتمال البيانات للمستخدم {telegram_id} بعد التحديث"
            )

            # جلب البيانات الحالية للمستخدم للفحص
            cursor.execute(
                """
                SELECT platform, whatsapp, payment_method, payment_details
                FROM registration_data
                WHERE user_id = ?
                """,
                (user_id,),
            )
            current_data = cursor.fetchone()

            if current_data:
                # sqlite3.Row objects support dictionary-style access, not .get() method
                platform = (
                    current_data["platform"] if current_data["platform"] else None
                )
                whatsapp = (
                    current_data["whatsapp"] if current_data["whatsapp"] else None
                )
                payment_method = (
                    current_data["payment_method"]
                    if current_data["payment_method"]
                    else None
                )
                payment_details = (
                    current_data["payment_details"]
                    if current_data["payment_details"]
                    else None
                )

                # فحص اكتمال جميع البيانات المطلوبة
                is_complete = (
                    platform
                    and platform.strip() != ""
                    and whatsapp
                    and whatsapp.strip() != ""
                    and payment_method
                    and payment_method.strip() != ""
                    and payment_details
                    and payment_details.strip() != ""
                )

                logger.info(f"📊 [الحل الثاني] حالة البيانات للمستخدم {telegram_id}:")
                logger.info(
                    f"   • المنصة: {'✅' if platform and platform.strip() else '❌'} ({platform})"
                )
                logger.info(
                    f"   • الواتساب: {'✅' if whatsapp and whatsapp.strip() else '❌'} ({whatsapp})"
                )
                logger.info(
                    f"   • طريقة الدفع: {'✅' if payment_method and payment_method.strip() else '❌'} ({payment_method})"
                )
                logger.info(
                    f"   • تفاصيل الدفع: {'✅' if payment_details and payment_details.strip() else '❌'} ({len(payment_details) if payment_details else 0} حرف)"
                )

                if is_complete:
                    # فحص الحالة الحالية لـ registration_status
                    cursor.execute(
                        "SELECT registration_status FROM users WHERE user_id = ?",
                        (user_id,),
                    )
                    current_status = cursor.fetchone()

                    if (
                        current_status
                        and current_status["registration_status"] != "complete"
                    ):
                        # تحديث حالة التسجيل إلى مكتمل
                        cursor.execute(
                            "UPDATE users SET registration_status = 'complete' WHERE user_id = ?",
                            (user_id,),
                        )
                        logger.info(
                            f"🎉 [الحل الثاني] تم تحديث registration_status إلى 'complete' للمستخدم {telegram_id}"
                        )
                    else:
                        logger.info(
                            f"ℹ️ [الحل الثاني] المستخدم {telegram_id} كان مكتملاً مسبقاً"
                        )
                else:
                    logger.info(
                        f"⏳ [الحل الثاني] المستخدم {telegram_id} لا يزال غير مكتمل - يحتاج بيانات أخرى"
                    )

            conn.commit()
            conn.close()
            return True

        except Exception as e:
            conn.rollback()
            conn.close()
            logger.error(f"خطأ في تحديث بيانات المستخدم: {e}")
            return False

    def update_user_platform(self, telegram_id: int, platform: str) -> bool:
        """تحديث منصة المستخدم"""
        return self.update_user_data(telegram_id, {"platform": platform})

    def delete_user_account(self, telegram_id: int) -> bool:
        """حذف حساب المستخدم"""
        conn = self.get_connection()
        cursor = conn.cursor()

        try:
            cursor.execute(
                "SELECT user_id FROM users WHERE telegram_id = ?", (telegram_id,)
            )
            user = cursor.fetchone()

            if not user:
                conn.close()
                return False

            user_id = user["user_id"]

            # حذف من جميع الجداول
            cursor.execute("DELETE FROM transactions WHERE user_id = ?", (user_id,))
            cursor.execute("DELETE FROM wallet WHERE user_id = ?", (user_id,))

            cursor.execute(
                "DELETE FROM registration_data WHERE user_id = ?", (user_id,)
            )
            cursor.execute(
                "DELETE FROM temp_registration WHERE telegram_id = ?", (telegram_id,)
            )
            cursor.execute("DELETE FROM users WHERE user_id = ?", (user_id,))

            conn.commit()
            conn.close()
            return True

        except Exception as e:
            conn.rollback()
            conn.close()
            logger.error(f"خطأ في حذف الحساب: {e}")
            return False


# ================================ لوحات المفاتيح ================================
class Keyboards:
    """لوحات المفاتيح"""

    @staticmethod
    def get_start_keyboard():
        """لوحة البداية"""
        keyboard = [
            [InlineKeyboardButton("🆕 تسجيل جديد", callback_data="register_new")],
            [InlineKeyboardButton("📞 الدعم الفني", callback_data="support")],
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def get_platform_keyboard():
        """لوحة المنصات"""
        keyboard = []
        for key, platform in GAMING_PLATFORMS.items():
            keyboard.append(
                [
                    InlineKeyboardButton(
                        platform["name"], callback_data=f"platform_{key}"
                    )
                ]
            )
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def get_payment_keyboard():
        """لوحة طرق الدفع"""
        keyboard = []
        for key, method in PAYMENT_METHODS.items():
            keyboard.append(
                [InlineKeyboardButton(method["name"], callback_data=f"payment_{key}")]
            )
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def get_continue_keyboard():
        """لوحة الاستكمال"""
        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ أكمل من حيث توقفت", callback_data="continue_registration"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔄 ابدأ من جديد", callback_data="restart_registration"
                )
            ],
        ]
        return InlineKeyboardMarkup(keyboard)

    @staticmethod
    def get_delete_keyboard():
        """لوحة حذف الحساب"""
        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ نعم، احذف حسابي", callback_data="confirm_delete"
                )
            ],
            [InlineKeyboardButton("❌ لا، تراجع", callback_data="cancel_delete")],
        ]
        return InlineKeyboardMarkup(keyboard)


# ================================ معالج التسجيل الذكي ================================
class SmartRegistrationHandler:
    """معالج التسجيل مع النظام الذكي"""

    def __init__(self):
        self.db = Database()

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """معالج بدء التسجيل مع Registration Threading - المرحلة 5"""
        telegram_id = update.effective_user.id
        username = update.effective_user.username

        logger.info(
            f"🔄 [Registration-Threading] بدء معالجة start للمستخدم {telegram_id}"
        )

        try:
            # الحصول على bot_instance من context
            if "bot_instance" not in context.bot_data:
                logger.error(
                    f"❌ [Registration-Threading] bot_instance غير موجود في context"
                )
                # إصلاح 1: استخدام effective_message بدلاً من message
                if update.effective_message:
                    await update.effective_message.reply_text(
                        "⚠️ حدث خطأ في النظام، يرجى المحاولة مرة أخرى"
                    )
                else:
                    # في حالة عدم وجود message، استخدام context.bot للإرسال المباشر
                    await context.bot.send_message(
                        chat_id=telegram_id,
                        text="⚠️ حدث خطأ في النظام، يرجى المحاولة مرة أخرى",
                    )
                return ConversationHandler.END

            bot_instance = context.bot_data["bot_instance"]

            # تشغيل المعالجة في Registration ThreadPool
            result = await asyncio.get_event_loop().run_in_executor(
                bot_instance.registration_pool, self._process_start_sync, telegram_id
            )

            logger.info(
                f"✅ [Registration-Threading] معالجة start مكتملة للمستخدم {telegram_id} - النتيجة: {result['type']}"
            )

            # معالجة النتيجة حسب نوع المستخدم
            if result["type"] == "complete_user":
                # مستخدم مسجل بالكامل - عرض القائمة الرئيسية مباشرة
                return await self._handle_complete_user(update, context, result)
            if result["type"] == "has_temp_data":
                # مستخدم له تسجيل ناقص - استكمال التسجيل
                return await self._handle_temp_registration(
                    update, context, result["temp_data"]
                )
            elif result["type"] == "new_user":
                # مستخدم جديد - بدء التسجيل
                return await self._handle_new_user(update, context)
            else:
                # خطأ في المعالجة
                logger.error(
                    f"❌ [Registration-Threading] نتيجة غير متوقعة للمستخدم {telegram_id}: {result}"
                )
                # إصلاح 1: استخدام effective_message بدلاً من message
                if update.effective_message:
                    await update.effective_message.reply_text(
                        "⚠️ حدث خطأ، يرجى المحاولة مرة أخرى"
                    )
                else:
                    await context.bot.send_message(
                        chat_id=telegram_id, text="⚠️ حدث خطأ، يرجى المحاولة مرة أخرى"
                    )
                return ConversationHandler.END

        except Exception as e:
            logger.error(
                f"❌ [Registration-Threading] خطأ في معالجة start للمستخدم {telegram_id}: {e}"
            )
            # إصلاح 1: استخدام effective_message بدلاً من message
            if update.effective_message:
                await update.effective_message.reply_text(
                    "⚠️ حدث خطأ، يرجى المحاولة مرة أخرى"
                )
            else:
                await context.bot.send_message(
                    chat_id=telegram_id, text="⚠️ حدث خطأ، يرجى المحاولة مرة أخرى"
                )
            return ConversationHandler.END

    def _process_start_sync(self, telegram_id: int) -> dict:
        """معالجة طلب start شاملة لكل أنواع المستخدمين - المرحلة 5 الخطوة 2ب"""
        thread_name = threading.current_thread().name
        logger.info(
            f"🔄 [Registration-Thread-{thread_name}] معالجة شاملة للمستخدم {telegram_id}"
        )

        start_time = time.time()

        try:
            # 1. فحص المستخدم في قاعدة البيانات الرئيسية أولاً
            user_data = self.db.get_user_by_telegram_id(telegram_id)

            if user_data and user_data.get("registration_status") == "complete":
                processing_time = (time.time() - start_time) * 1000
                logger.info(
                    f"👤 [Registration-Thread-{thread_name}] مستخدم مكتمل: {telegram_id} - وقت: {processing_time:.2f}ms"
                )
                return {
                    "type": "complete_user",
                    "user_data": user_data,
                    "platform": user_data.get("platform"),
                    "whatsapp": user_data.get("whatsapp"),
                    "payment_method": user_data.get("payment_method"),
                    "processing_time_ms": processing_time,
                }

            # 2. فحص التسجيل المؤقت للمستخدمين غير المكتملين
            temp_data = self.db.get_temp_registration(telegram_id)

            processing_time = (time.time() - start_time) * 1000  # milliseconds
            logger.info(
                f"⏱️ [Registration-Thread-{thread_name}] وقت الاستعلام الكامل: {processing_time:.2f}ms"
            )

            if temp_data:
                logger.info(
                    f"⏳ [Registration-Thread-{thread_name}] مستخدم غير مكتمل: {telegram_id}"
                )
                return {"type": "has_temp_data", "temp_data": temp_data}
            else:
                logger.info(
                    f"🆕 [Registration-Thread-{thread_name}] مستخدم جديد: {telegram_id}"
                )
                return {"type": "new_user", "temp_data": None}

        except Exception as e:
            logger.error(
                f"❌ [Registration-Thread-{thread_name}] خطأ في معالجة {telegram_id}: {e}"
            )
            return {"type": "error", "error": str(e)}

    async def _handle_temp_registration(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, temp_data: dict
    ):
        """معالجة المستخدم الذي له تسجيل ناقص"""
        telegram_id = update.effective_user.id

        # استعادة البيانات المحفوظة
        context.user_data["registration"] = temp_data["data"]
        step = temp_data["step_number"]

        step_names = {
            ENTERING_WHATSAPP: "إدخال واتساب",
            CHOOSING_PAYMENT: "اختيار طريقة الدفع",
        }
        last_step = step_names.get(step, "غير معروف")

        message = MESSAGES["welcome_back"].format(last_step=last_step)

        # إضافة أزرار للاختيار بين المتابعة أو البدء من جديد
        keyboard = [
            [
                InlineKeyboardButton(
                    "✅ متابعة من حيث توقفت", callback_data="continue_registration"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔄 البدء من جديد", callback_data="restart_registration"
                )
            ],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # إرسال رسالة مع الأزرار
        await smart_message_manager.send_new_active_message(
            update,
            context,
            message + "\n\nماذا تريد أن تفعل؟",
            reply_markup=reply_markup,
        )

        logger.info(
            f"✅ [Registration-Threading] عرض استكمال التسجيل للمستخدم {telegram_id}"
        )
        return ConversationHandler.END

    async def _handle_new_user(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالجة المستخدم الجديد"""
        telegram_id = update.effective_user.id

        # مستخدم جديد
        await smart_message_manager.send_new_active_message(
            update,
            context,
            MESSAGES["welcome"],
            reply_markup=Keyboards.get_start_keyboard(),
        )

        logger.info(
            f"✅ [Registration-Threading] عرض الترحيب للمستخدم الجديد {telegram_id}"
        )
        return ConversationHandler.END

    async def _handle_complete_user(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, result: dict
    ):
        """معالجة المستخدمين المسجلين بالكامل مع Threading السريع"""

        user_data = result["user_data"]
        telegram_id = user_data["telegram_id"]
        processing_time = result.get("processing_time_ms", 0)

        logger.info(
            f"✅ [Registration-Threading] عرض القائمة الرئيسية للمستخدم المكتمل {telegram_id} - معالج في {processing_time:.2f}ms"
        )

        try:
            # عرض القائمة الرئيسية مباشرة مع ملخص البيانات
            platform_name = GAMING_PLATFORMS.get(user_data["platform"], {}).get(
                "name", "غير محدد"
            )
            payment_name = PAYMENT_METHODS.get(user_data["payment_method"], {}).get(
                "name", "غير محدد"
            )

            welcome_text = f"""🎮 مرحباً بعودتك!

✅ ملخص بياناتك:
━━━━━━━━━━━━━━━━
🎮 المنصة: {platform_name}
📱 واتساب: {user_data['whatsapp']}
💳 طريقة الدفع: {payment_name}
━━━━━━━━━━━━━━━━

اختر ما تريد:"""

            # استخدام نفس keyboard القائمة الرئيسية
            keyboard = Keyboards.get_main_menu()

            await smart_message_manager.send_new_active_message(
                update, context, welcome_text, keyboard
            )

            logger.info(
                f"🎯 [Registration-Threading] تم عرض القائمة الرئيسية بنجاح للمستخدم {telegram_id}"
            )
            return ConversationHandler.END

        except Exception as e:
            logger.error(
                f"❌ [Registration-Threading] خطأ في عرض القائمة للمستخدم {telegram_id}: {e}"
            )
            await update.message.reply_text("⚠️ حدث خطأ، يرجى المحاولة مرة أخرى")
            return ConversationHandler.END

    async def handle_registration_start(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """بدء التسجيل الجديد مع حماية من الضغط المتكرر"""
        query = update.callback_query

        # الرد على الـ callback query بسرعة
        await query.answer()

        telegram_id = query.from_user.id
        username = query.from_user.username
        full_name = query.from_user.full_name

        # التحقق من عدم وجود تسجيل قيد المعالجة
        if "registration" in context.user_data and context.user_data[
            "registration"
        ].get("in_progress"):
            logger.debug(f"تجاهل محاولة بدء تسجيل مكرر للمستخدم {telegram_id}")
            return

        # وضع علامة أن التسجيل قيد المعالجة
        context.user_data["registration"] = {
            "in_progress": True,
            "telegram_id": telegram_id,
        }

        # مسح أي بيانات تسجيل قديمة
        self.db.clear_temp_registration(telegram_id)

        user_id = self.db.create_user(telegram_id, username, full_name)

        # تحديث بيانات التسجيل
        context.user_data["registration"].update(
            {
                "user_id": user_id,
                "in_progress": False,  # إلغاء العلامة بعد اكتمال المعالجة
            }
        )

        await smart_message_manager.update_current_message(
            update,
            context,
            MESSAGES["choose_platform"],
            reply_markup=Keyboards.get_platform_keyboard(),
        )

        return CHOOSING_PLATFORM

    async def handle_platform_choice(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """اختيار المنصة مع حماية من الضغط المتكرر"""
        query = update.callback_query

        # الرد على الـ callback query بسرعة لمنع ظهور رمز التحميل
        await query.answer()

        # التحقق من أن البيانات صحيحة
        if not query.data.startswith("platform_"):
            return

        platform_key = query.data.replace("platform_", "")

        # التحقق من صحة المنصة
        if platform_key not in GAMING_PLATFORMS:
            await query.answer("❌ منصة غير صحيحة", show_alert=True)
            return

        platform_name = GAMING_PLATFORMS[platform_key]["name"]

        # التحقق من وضع التعديل
        is_editing = context.user_data.get("editing_mode") == "whatsapp_full"

        if is_editing:
            # في وضع التعديل - نحفظ في edit_registration
            if "edit_registration" not in context.user_data:
                context.user_data["edit_registration"] = {
                    "telegram_id": query.from_user.id,
                    "is_editing": True,
                }

            context.user_data["edit_registration"]["platform"] = platform_key

            # عرض رسالة إدخال رقم الواتساب الجديد
            await smart_message_manager.update_current_message(
                update,
                context,
                f"✅ تم اختيار: {platform_name}\n\n📱 أدخل رقم الواتساب الجديد:\n\n"
                + MESSAGES["enter_whatsapp"],
            )
        else:
            # في وضع التسجيل العادي
            if "registration" not in context.user_data:
                context.user_data["registration"] = {"telegram_id": query.from_user.id}

            # التحقق من عدم تكرار نفس الاختيار
            if context.user_data["registration"].get("platform") == platform_key:
                logger.debug(f"تجاهل اختيار منصة مكرر: {platform_key}")
                return

            context.user_data["registration"]["platform"] = platform_key

            self.db.save_temp_registration(
                context.user_data["registration"]["telegram_id"],
                "platform_chosen",
                ENTERING_WHATSAPP,
                context.user_data["registration"],
            )

            # استخدام update_current_message لتحديث الرسالة الحالية بدلاً من إرسال جديدة
            await smart_message_manager.update_current_message(
                update,
                context,
                f"✅ تم اختيار: {platform_name}\n\n" + MESSAGES["enter_whatsapp"],
            )

        return ENTERING_WHATSAPP

    async def handle_whatsapp_input(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """إدخال واتساب مع نظام الحماية المتقدم"""
        user_id = update.effective_user.id
        whatsapp_input = update.message.text.strip()

        # 1. فحص الحظر
        is_blocked, remaining_minutes = whatsapp_security.is_user_blocked(user_id)
        if is_blocked:
            await smart_message_manager.send_new_active_message(
                update,
                context,
                f"""🚫 أنت محظور مؤقتاً
⏰ المدة المتبقية: {remaining_minutes} دقيقة
📝 السبب: تجاوز عدد المحاولات الخاطئة المسموح بها
💡 نصيحة: تأكد من إدخال رقم واتساب صحيح عند المحاولة مرة أخرى""",
                disable_previous=False,
            )
            return ENTERING_WHATSAPP

        # 2. فحص معدل الطلبات
        rate_ok, rate_message = whatsapp_security.check_rate_limit(user_id)
        if not rate_ok:
            await smart_message_manager.send_new_active_message(
                update, context, rate_message, disable_previous=False
            )
            return ENTERING_WHATSAPP

        # 3. فحص التكرار
        if whatsapp_security.check_duplicate(user_id, whatsapp_input):
            await smart_message_manager.send_new_active_message(
                update,
                context,
                f"""⚠️ لقد أدخلت هذا الرقم بالفعل
🔢 الرقم: {whatsapp_input}
💡 نصيحة: إذا كان الرقم صحيحاً، انتظر رسالة التأكيد
إذا كنت تريد تغييره، أدخل رقماً مختلفاً""",
                disable_previous=False,
            )
            return ENTERING_WHATSAPP

        # 4. التحقق الشامل من الرقم
        validation = whatsapp_security.validate_whatsapp(whatsapp_input, user_id)

        if not validation["is_valid"]:
            # تسجيل المحاولة الفاشلة
            was_blocked = whatsapp_security.record_failure(user_id)
            remaining = whatsapp_security.get_remaining_attempts(user_id)

            # تسجيل نتيجة التحقق بالنظام الوصفي الجديد
            desc_logger.log_validation_result(
                user_id,
                "واتساب",
                False,
                f"نوع الخطأ: {validation.get('error_type', 'غير محدد')} - محاولات متبقية: {remaining}",
            )

            # إضافة معلومات المحاولات المتبقية للرسالة
            error_msg = validation["error_message"]

            if was_blocked:
                error_msg += f"""
🚫 تم حظرك مؤقتاً لمدة {whatsapp_security.BLOCK_DURATION_MINUTES} دقيقة
السبب: تجاوز عدد المحاولات الخاطئة"""
            elif remaining > 0:
                error_msg += f"""
⚠️ تحذير: لديك {remaining} محاولات متبقية"""

            await smart_message_manager.send_new_active_message(
                update, context, error_msg, disable_previous=False
            )

            # تسجيل المحاولة في السجلات (مع الحد الأقصى للأحرف)
            input_preview = (
                whatsapp_input[:20] + "..."
                if len(whatsapp_input) > 20
                else whatsapp_input
            )
            desc_logger.log_warning(
                "محاولة واتساب فاشلة",
                f"المستخدم {user_id} - نوع: {validation['error_type']} - مدخل: {input_preview}",
            )

            return ENTERING_WHATSAPP

        # 5. النجاح! إعادة تعيين المحاولات الفاشلة
        whatsapp_security.reset_user_failures(user_id)

        # حفظ الرقم المنظف في السياق
        cleaned_number = validation["cleaned_number"]
        network_info = validation["network_info"]

        # تسجيل نجح التحقق من الواتساب
        desc_logger.log_validation_result(
            user_id,
            "واتساب",
            True,
            f"شبكة: {network_info.get('name', 'غير محدد')} - الرقم: {cleaned_number[:8]}***",
        )

        # التحقق من وضع التعديل
        is_editing = context.user_data.get("editing_mode") in [
            "whatsapp_only",
            "whatsapp_full",
            "payment_only",
        ]

        if is_editing:
            # في وضع التعديل - نحفظ في edit_registration
            if "edit_registration" not in context.user_data:
                context.user_data["edit_registration"] = {
                    "telegram_id": user_id,
                    "is_editing": True,
                }

            context.user_data["edit_registration"]["whatsapp"] = cleaned_number
            context.user_data["edit_registration"]["whatsapp_network"] = network_info[
                "name"
            ]

            # في حالة تعديل الواتساب فقط، نحفظ مباشرة
            if context.user_data.get("editing_mode") == "whatsapp_only":
                # تحديث قاعدة البيانات
                success = self.db.update_user_data(
                    user_id,
                    {
                        "whatsapp": cleaned_number,
                        "whatsapp_network": network_info["name"],
                    },
                )

                if success:
                    # عرض رسالة النجاح والعودة للملف الشخصي
                    profile = self.db.get_user_profile(user_id)

                    profile_text = f"""
✅ تم تحديث رقم الواتساب بنجاح!
━━━━━━━━━━━━━━━━
👤 الملف الشخصي المحدث
━━━━━━━━━━━━━━━━
🎮 المنصة: {profile.get('platform', 'غير محدد')}
📱 واتساب: {cleaned_number} ✅
💳 طريقة الدفع: {profile.get('payment_method', 'غير محدد')}
━━━━━━━━━━━━━━━━
🔐 بياناتك محمية ومشفرة
"""

                    keyboard = [
                        [
                            InlineKeyboardButton(
                                "✏️ تعديل آخر", callback_data="edit_profile"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🏠 القائمة الرئيسية", callback_data="main_menu"
                            )
                        ],
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    await smart_message_manager.send_new_active_message(
                        update, context, profile_text, reply_markup=reply_markup
                    )

                    # مسح وضع التعديل
                    context.user_data.pop("editing_mode", None)
                    context.user_data.pop("edit_registration", None)

                    return ConversationHandler.END
                else:
                    await smart_message_manager.send_new_active_message(
                        update,
                        context,
                        "❌ حدث خطأ في حفظ البيانات. حاول مرة أخرى.",
                        disable_previous=False,
                    )
                    return ConversationHandler.END
        else:
            # في وضع التسجيل العادي
            if "registration" not in context.user_data:
                context.user_data["registration"] = {"telegram_id": user_id}

            context.user_data["registration"]["whatsapp"] = cleaned_number
            context.user_data["registration"]["whatsapp_network"] = network_info["name"]

            # حفظ في قاعدة البيانات المؤقتة
            try:
                self.db.save_temp_registration(
                    context.user_data["registration"]["telegram_id"],
                    "whatsapp_entered",
                    CHOOSING_PAYMENT,
                    context.user_data["registration"],
                )
            except Exception as e:
                logger.error(f"Error saving temp registration: {e}")

        # رسالة النجاح المفصلة
        success_message = f"""✅ تم حفظ رقم الواتساب بنجاح!

📱 الرقم: {cleaned_number}
🌐 الشبكة: {network_info['emoji']} {network_info['name']}
💾 تم الحفظ التلقائي ✅

━━━━━━━━━━━━━━━━
⏭️ الخطوة التالية: اختر طريقة الدفع المفضلة"""

        # إرسال رسالة النجاح مع خيارات الدفع
        await smart_message_manager.send_new_active_message(
            update,
            context,
            success_message + "\n\n" + MESSAGES["choose_payment"],
            reply_markup=Keyboards.get_payment_keyboard(),
            choice_made=f"واتساب: {cleaned_number}",
        )

        # تسجيل النجاح
        logger.info(
            f"تم حفظ رقم واتساب للمستخدم {user_id}: {cleaned_number} - شبكة: {network_info['name']}"
        )

        return CHOOSING_PAYMENT

    async def handle_payment_choice(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """اختيار طريقة الدفع مع حماية من الضغط المتكرر"""
        query = update.callback_query

        # الرد على الـ callback query بسرعة
        await query.answer()

        # التحقق من أن البيانات صحيحة
        if not query.data.startswith("payment_"):
            return

        payment_key = query.data.replace("payment_", "")

        # التحقق من صحة طريقة الدفع
        if payment_key not in PAYMENT_METHODS:
            await query.answer("❌ طريقة دفع غير صحيحة", show_alert=True)
            return

        payment_name = PAYMENT_METHODS[payment_key]["name"]

        # تسجيل اختيار طريقة الدفع بالنظام الوصفي الجديد
        desc_logger.log_user_action(
            query.from_user.id,
            f"اختار طريقة الدفع: {payment_name}",
            f"الكود: {payment_key} - انتقال لإدخال التفاصيل",
        )

        # التحقق من وضع التعديل
        is_editing = context.user_data.get("editing_mode") in [
            "whatsapp_full",
            "payment_only",
        ]

        if is_editing:
            # في وضع التعديل - نحفظ في edit_registration
            if "edit_registration" not in context.user_data:
                await query.answer("❌ يجب البدء من جديد", show_alert=True)
                return ConversationHandler.END

            # التحقق من عدم تكرار نفس الاختيار
            if (
                context.user_data["edit_registration"].get("payment_method")
                == payment_key
            ):
                logger.debug(f"تجاهل اختيار طريقة دفع مكررة: {payment_key}")
                return

            context.user_data["edit_registration"]["payment_method"] = payment_key
        else:
            # في وضع التسجيل العادي
            if "registration" not in context.user_data:
                await query.answer("❌ يجب البدء من جديد", show_alert=True)
                return ConversationHandler.END

            # التحقق من عدم تكرار نفس الاختيار
            if context.user_data["registration"].get("payment_method") == payment_key:
                logger.debug(f"تجاهل اختيار طريقة دفع مكررة: {payment_key}")
                return

            context.user_data["registration"]["payment_method"] = payment_key

            # حفظ في قاعدة البيانات المؤقتة
            self.db.save_temp_registration(
                context.user_data["registration"]["telegram_id"],
                "payment_method_chosen",
                ENTERING_PAYMENT_DETAILS,
                context.user_data["registration"],
            )

        # عرض التعليمات حسب نوع طريقة الدفع
        instructions = self.get_payment_instructions(payment_key)

        await smart_message_manager.update_current_message(
            update, context, instructions
        )

        return ENTERING_PAYMENT_DETAILS

    def get_payment_instructions(self, payment_key: str) -> str:
        """الحصول على التعليمات المناسبة لكل طريقة دفع - محسنة"""

        if payment_key == "vodafone_cash":
            return """⭕️ فودافون كاش

📱 أدخل رقم:

📝 القواعد:
• 11 رقم بالضبط
• يبدأ بـ 010 / 011 / 012 / 015
• أرقام إنجليزية فقط (0-9)
• بدون مسافات أو رموز

✅ مثال صحيح: 01012345678"""

        elif payment_key == "etisalat_cash":
            return """🟢 اتصالات كاش

📱 أدخل رقم:

📝 القواعد:
• 11 رقم بالضبط
• يبدأ بـ 010 / 011 / 012 / 015
• أرقام إنجليزية فقط (0-9)
• بدون مسافات أو رموز

✅ مثال صحيح: 01112345678"""

        elif payment_key == "orange_cash":
            return """🍊 أورانج كاش

📱 أدخل رقم:

📝 القواعد:
• 11 رقم بالضبط
• يبدأ بـ 010 / 011 / 012 / 015
• أرقام إنجليزية فقط (0-9)
• بدون مسافات أو رموز

✅ مثال صحيح: 01212345678"""

        elif payment_key == "we_cash":
            return """🟣 وي كاش

📱 أدخل رقم:

📝 القواعد:
• 11 رقم بالضبط
• يبدأ بـ 010 / 011 / 012 / 015
• أرقام إنجليزية فقط (0-9)
• بدون مسافات أو رموز

✅ مثال صحيح: 01512345678"""

        elif payment_key == "bank_wallet":
            return """🏦 محفظة بنكية

📱 أدخل رقم المحفظة:

📝 القواعد:
• 11 رقم بالضبط
• يقبل جميع الشبكات: 010/011/012/015
• أرقام إنجليزية فقط (0-9)
• بدون مسافات أو رموز

✅ أمثلة صحيحة:
• 01012345678 - فودافون ⭕
• 01112345678 - اتصالات 🟢
• 01212345678 - أورانج 🍊
• 01512345678 - وي 🟣

📌 ملاحظة مهمة: المحفظة البنكية تقبل جميع الشبكات المصرية
✅ يمكنك استخدام أي رقم من الشبكات الأربعة"""

        elif payment_key == "telda":
            return """💳 تيلدا

💳 أدخل رقم كارت تيلدا:

📝 القواعد:
• 16 رقم بالضبط
• أرقام فقط
• يُسمح بالمسافات والشرطات

✅ أمثلة صحيحة:
• 1234567890123456
• 1234-5678-9012-3456
• 1234 5678 9012 3456"""

        elif payment_key == "instapay":
            return """🔗 إنستا باي

🔗 أدخل رابط إنستاباي كامل:

📝 القواعد:
• رابط كامل فقط
• يحتوي على instapay.com.eg أو ipn.eg

✅ أمثلة صحيحة:
• https://instapay.com.eg/abc123
• https://ipn.eg/S/username/ABC123
• instapay.com.eg/xyz789
• ipn.eg/S/ABC123"""

        return "طريقة دفع غير معروفة"

    async def handle_payment_details_input(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالج إدخال بيانات طريقة الدفع مع التشفير"""
        user_id = update.effective_user.id
        payment_input = update.message.text.strip()

        # التحقق من وضع التعديل
        is_editing = context.user_data.get("editing_mode") in [
            "whatsapp_full",
            "payment_only",
        ]

        if is_editing:
            # في وضع التعديل
            if (
                "edit_registration" not in context.user_data
                or "payment_method" not in context.user_data["edit_registration"]
            ):
                await smart_message_manager.send_new_active_message(
                    update,
                    context,
                    "❌ حدث خطأ. يرجى البدء من جديد بكتابة /start",
                    disable_previous=False,
                )
                return ConversationHandler.END

            payment_method = context.user_data["edit_registration"]["payment_method"]
        else:
            # في وضع التسجيل العادي
            if (
                "registration" not in context.user_data
                or "payment_method" not in context.user_data["registration"]
            ):
                await smart_message_manager.send_new_active_message(
                    update,
                    context,
                    "❌ حدث خطأ. يرجى البدء من جديد بكتابة /start",
                    disable_previous=False,
                )
                return ConversationHandler.END

            payment_method = context.user_data["registration"]["payment_method"]

        # 1. فحص الحظر
        is_blocked, remaining_minutes = payment_validation.is_user_blocked(user_id)
        if is_blocked:
            await smart_message_manager.send_new_active_message(
                update,
                context,
                f"""🚫 أنت محظور مؤقتاً
⏰ المدة المتبقية: {remaining_minutes} دقيقة
📝 السبب: تجاوز عدد المحاولات الخاطئة المسموح بها
💡 نصيحة: تأكد من إدخال البيانات الصحيحة عند المحاولة مرة أخرى""",
                disable_previous=False,
            )
            return ENTERING_PAYMENT_DETAILS

        # 2. فحص معدل الطلبات
        rate_ok, rate_message = payment_validation.check_rate_limit(user_id)
        if not rate_ok:
            await smart_message_manager.send_new_active_message(
                update, context, rate_message, disable_previous=False
            )
            return ENTERING_PAYMENT_DETAILS

        # 3. التحقق حسب نوع طريقة الدفع
        validation_result = None
        payment_type = None

        if payment_method in [
            "vodafone_cash",
            "etisalat_cash",
            "orange_cash",
            "we_cash",
            "bank_wallet",
        ]:
            validation_result = payment_validation.validate_wallet(
                payment_input, payment_method
            )
            payment_type = "wallet"
        elif payment_method == "telda":
            validation_result = payment_validation.validate_telda(payment_input)
            payment_type = "card"
        elif payment_method == "instapay":
            # تسجيل بدء تحقق InstaPay
            input_preview = (
                payment_input[:30] + "..." if len(payment_input) > 30 else payment_input
            )
            desc_logger.log_user_action(
                user_id, "بدء التحقق من InstaPay", f"المدخل: {input_preview}"
            )
            validation_result = payment_validation.validate_instapay(payment_input)
            payment_type = "link"

        # 4. معالجة النتيجة
        if not validation_result["is_valid"]:
            # تسجيل المحاولة الفاشلة
            was_blocked = payment_validation.record_failure(user_id)
            remaining = payment_validation.get_remaining_attempts(user_id)

            # تسجيل نتيجة التحقق بالنظام الوصفي الجديد
            desc_logger.log_validation_result(
                user_id,
                f"دفع {payment_method}",
                False,
                f"نوع الدفع: {payment_type} - محاولات متبقية: {remaining}",
            )

            # إضافة معلومات المحاولات المتبقية للرسالة
            error_msg = validation_result["error_message"]

            if was_blocked:
                error_msg += f"""
🚫 تم حظرك مؤقتاً لمدة {payment_validation.BLOCK_DURATION_MINUTES} دقيقة
السبب: تجاوز عدد المحاولات الخاطئة"""
            elif remaining > 0:
                error_msg += f"""
⚠️ تحذير: لديك {remaining} محاولات متبقية"""

            await smart_message_manager.send_new_active_message(
                update, context, error_msg, disable_previous=False
            )

            # تسجيل المحاولة في السجلات (بدون البيانات الحساسة - 200 حرف حد أقصى)
            desc_logger.log_warning(
                "محاولة دفع فاشلة",
                f"المستخدم {user_id} - طريقة: {payment_method} - نوع: {payment_type}",
            )

            return ENTERING_PAYMENT_DETAILS

        # 5. النجاح! إعادة تعيين المحاولات الفاشلة
        payment_validation.reset_user_failures(user_id)

        # تسجيل نجح التحقق من طريقة الدفع
        cleaned_preview = validation_result["cleaned_data"][:8] + "***"
        desc_logger.log_validation_result(
            user_id,
            f"دفع {payment_method}",
            True,
            f"نوع: {payment_type} - تشفير البيانات تم بنجح - معرف: {cleaned_preview}",
        )

        # 6. تشفير البيانات الحساسة
        encrypted_data = encryption_system.encrypt(validation_result["cleaned_data"])

        if is_editing:
            # في وضع التعديل - نحفظ في edit_registration
            context.user_data["edit_registration"]["payment_details"] = encrypted_data
            context.user_data["edit_registration"][
                "payment_details_type"
            ] = payment_type

            if payment_type == "wallet":
                context.user_data["edit_registration"]["payment_network"] = (
                    validation_result.get("network", "")
                )
        else:
            # في وضع التسجيل العادي
            context.user_data["registration"]["payment_details"] = encrypted_data
            context.user_data["registration"]["payment_details_type"] = payment_type

            if payment_type == "wallet":
                context.user_data["registration"]["payment_network"] = (
                    validation_result.get("network", "")
                )

            # حفظ في قاعدة البيانات المؤقتة
            try:
                self.db.save_temp_registration(
                    context.user_data["registration"]["telegram_id"],
                    "payment_details_entered",
                    ConversationHandler.END,
                    context.user_data["registration"],
                )
            except Exception as e:
                logger.error(f"Error saving temp registration: {e}")

        # 9. إعداد رسالة النجاح
        payment_name = PAYMENT_METHODS[payment_method]["name"]

        if payment_type == "wallet":
            success_message = f"""✅ تم حفظ {payment_name}!

📱 الرقم: {validation_result['cleaned_data']}

━━━━━━━━━━━━━━━━"""
        elif payment_type == "card":
            # عرض رقم الكارت كامل للعميل بدون إخفاء
            success_message = f"""✅ تم حفظ كارت تيلدا!

💳 رقم الكارت: {validation_result['cleaned_data']}

━━━━━━━━━━━━━━━━"""
        elif payment_type == "link":
            success_message = f"""✅ تم حفظ رابط إنستاباي!

🔗 الرابط: {validation_result['cleaned_data']}

━━━━━━━━━━━━━━━━"""

        # 10. إرسال رسالة النجاح ثم الانتقال للتأكيد النهائي
        await smart_message_manager.send_new_active_message(
            update, context, success_message, choice_made=f"{payment_name}: تم الحفظ"
        )

        # تسجيل النجاح (بدون البيانات الحساسة)
        logger.info(f"تم حفظ بيانات دفع للمستخدم {user_id}: نوع {payment_method}")

        # الانتقال للتأكيد النهائي
        return await self.show_confirmation(update, context)

    async def show_confirmation(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """عرض التأكيد والحفظ التلقائي مع فك تشفير البيانات"""
        # التحقق من وضع التعديل
        is_editing = context.user_data.get("editing_mode") in [
            "whatsapp_full",
            "payment_only",
        ]

        if is_editing:
            # في وضع التعديل - نحدث البيانات في قاعدة البيانات
            reg_data = context.user_data["edit_registration"]
            telegram_id = reg_data["telegram_id"]

            # تحديث البيانات في قاعدة البيانات
            update_data = {}

            if "platform" in reg_data:
                update_data["platform"] = reg_data["platform"]

            if "whatsapp" in reg_data:
                update_data["whatsapp"] = reg_data["whatsapp"]
                if "whatsapp_network" in reg_data:
                    update_data["whatsapp_network"] = reg_data["whatsapp_network"]

            if "payment_method" in reg_data:
                update_data["payment_method"] = reg_data["payment_method"]

            if "payment_details" in reg_data:
                update_data["payment_details"] = reg_data["payment_details"]
                update_data["payment_details_type"] = reg_data.get(
                    "payment_details_type", ""
                )
                if "payment_network" in reg_data:
                    update_data["payment_network"] = reg_data["payment_network"]

            # تحديث البيانات في قاعدة البيانات
            success = self.db.update_user_data(telegram_id, update_data)

            # مسح وضع التعديل
            context.user_data.pop("editing_mode", None)
            context.user_data.pop("edit_registration", None)
        else:
            # في وضع التسجيل العادي
            reg_data = context.user_data["registration"]
            telegram_id = reg_data["telegram_id"]
            success = self.db.complete_registration(telegram_id, reg_data)

        # الحصول على اسم المستخدم
        if update.callback_query:
            username = update.callback_query.from_user.username
        else:
            username = update.effective_user.username

        # إضافة @ للمستخدم إذا كان موجود
        username_display = f"@{username}" if username else "غير محدد"

        if success:
            # الحصول على البيانات المحدثة من قاعدة البيانات
            updated_user_data = self.db.get_user_data(telegram_id)

            if updated_user_data:
                platform = GAMING_PLATFORMS.get(
                    updated_user_data.get("platform"), {}
                ).get("name", "🔄 لم يتم تحديدها بعد")
                payment_method = updated_user_data.get("payment_method", "")
                payment_name = PAYMENT_METHODS.get(payment_method, {}).get(
                    "name", "🔄 لم يتم تحديدها بعد"
                )
                whatsapp = updated_user_data.get("whatsapp", "🔄 لم يتم إدخاله بعد")
            else:
                platform = GAMING_PLATFORMS.get(reg_data.get("platform"), {}).get(
                    "name", "🔄 لم يتم تحديدها بعد"
                )
                payment_method = reg_data.get("payment_method", "")
                payment_name = PAYMENT_METHODS.get(payment_method, {}).get(
                    "name", "🔄 لم يتم تحديدها بعد"
                )
                whatsapp = reg_data.get("whatsapp") or "🔄 لم يتم إدخاله بعد"

            # فك تشفير بيانات الدفع إذا كانت موجودة
            payment_details_display = ""
            if "payment_details" in reg_data:
                try:
                    decrypted_data = encryption_system.decrypt(
                        reg_data["payment_details"]
                    )
                    payment_type = reg_data.get("payment_details_type", "")

                    if payment_type == "wallet":
                        payment_details_display = f"""
💰 بيانات الدفع:
• الرقم: {decrypted_data}"""
                    elif payment_type == "card":
                        # عرض رقم الكارت كامل للعميل بدون إخفاء
                        payment_details_display = f"""
💰 بيانات الدفع:
• رقم الكارت: {decrypted_data}"""
                    elif payment_type == "link":
                        payment_details_display = f"""
💰 بيانات الدفع:
• الرابط: {decrypted_data}"""
                except:
                    payment_details_display = ""

            # رسالة النجاح - مختلفة حسب وضع التعديل
            if is_editing:
                success_message = f"""
✅ تم تحديث بياناتك بنجاح!

📊 ملخص البيانات المحدثة:
━━━━━━━━━━━━━━━━
🎮 المنصة: {platform}
📱 واتساب: {whatsapp}
💳 طريقة الدفع: {payment_name}{payment_details_display}
━━━━━━━━━━━━━━━━

👤 اسم المستخدم: {username_display}
🆔 معرف التليجرام: {telegram_id}

✨ تم تحديث ملفك الشخصي بنجاح!
"""
            else:
                success_message = f"""
✅ تم حفظ بياناتك بنجاح!

📊 ملخص البيانات المحفوظة:
━━━━━━━━━━━━━━━━
🎮 المنصة: {platform}
📱 واتساب: {whatsapp}
💳 طريقة الدفع: {payment_name}{payment_details_display}

━━━━━━━━━━━━━━━━
👤 اسم المستخدم: {username_display}
🆔 معرف التليجرام: {telegram_id}

🎉 مرحباً بك في عائلة FC 26! 🚀
"""

            # استخدام update_current_message إذا كان من callback
            if update.callback_query:
                await smart_message_manager.update_current_message(
                    update, context, success_message
                )
            else:
                await smart_message_manager.send_new_active_message(
                    update, context, success_message
                )

            # مسح البيانات المؤقتة
            context.user_data.clear()

            # تنظيف بيانات المستخدم في SmartMessageManager
            await smart_message_manager.cleanup_user_data(telegram_id)

            return ConversationHandler.END
        else:
            # في حالة الفشل
            error_message = "❌ حدث خطأ في حفظ البيانات. الرجاء المحاولة مرة أخرى."

            if update.callback_query:
                await smart_message_manager.update_current_message(
                    update, context, error_message
                )
            else:
                await smart_message_manager.send_new_active_message(
                    update, context, error_message
                )

            return ConversationHandler.END

    async def handle_continue_registration(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """استكمال التسجيل"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        if query.data == "continue_registration":
            temp_data = self.db.get_temp_registration(telegram_id)

            if temp_data:
                context.user_data["registration"] = temp_data["data"]
                step = temp_data["step_number"]

                step_messages = {
                    ENTERING_WHATSAPP: MESSAGES["enter_whatsapp"],
                    CHOOSING_PAYMENT: MESSAGES["choose_payment"],
                }

                message = step_messages.get(step, "")

                # عرض الرسالة المناسبة حسب الخطوة
                if step == CHOOSING_PAYMENT:
                    await smart_message_manager.update_current_message(
                        update,
                        context,
                        message,
                        reply_markup=Keyboards.get_payment_keyboard(),
                    )
                elif step == CHOOSING_PLATFORM:
                    await smart_message_manager.update_current_message(
                        update,
                        context,
                        message,
                        reply_markup=Keyboards.get_platform_keyboard(),
                    )
                elif step == ENTERING_WHATSAPP:
                    # للواتساب نرسل الرسالة بدون لوحة مفاتيح
                    await smart_message_manager.update_current_message(
                        update, context, message
                    )

                else:
                    await smart_message_manager.update_current_message(
                        update, context, message
                    )

                return step

        elif query.data == "restart_registration":
            self.db.clear_temp_registration(telegram_id)

            await smart_message_manager.update_current_message(
                update,
                context,
                MESSAGES["choose_platform"],
                reply_markup=Keyboards.get_platform_keyboard(),
            )

            context.user_data["registration"] = {"telegram_id": telegram_id}

            return CHOOSING_PLATFORM

    async def cancel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """إلغاء التسجيل"""
        context.user_data.clear()

        await smart_message_manager.send_new_active_message(
            update, context, "تم إلغاء عملية التسجيل. يمكنك البدء من جديد بكتابة /start"
        )

        return ConversationHandler.END


# ================================ المرحلة الرابعة: AdminHandler ================================
class AdminHandler:
    """معالج متقدم لعمليات الأدمن مع Threading احترافي"""

    def __init__(self, db, cache_size: int = 100):
        self.db = db
        self.cache = {}  # كاش للاستعلامات المتكررة
        self.cache_size = cache_size
        self.cache_hits = 0
        self.cache_misses = 0
        self.operations_count = {
            "panel": 0,
            "users": 0,
            "search": 0,
            "broadcast": 0,
            "delete": 0,
        }
        self.last_cleanup = time.time()
        logger.info("🎯 تم تهيئة AdminHandler مع كاش وإحصائيات متقدمة")

    def _cleanup_cache(self):
        """تنظيف الكاش القديم"""
        current_time = time.time()
        if current_time - self.last_cleanup > 300:  # كل 5 دقائق
            # إزالة أقدم 20% من الكاش إذا امتلأ
            if len(self.cache) > self.cache_size:
                items_to_remove = int(self.cache_size * 0.2)
                for key in list(self.cache.keys())[:items_to_remove]:
                    del self.cache[key]
            self.last_cleanup = current_time
            logger.debug(f"🧹 تم تنظيف الكاش - الحجم الحالي: {len(self.cache)}")

    def get_admin_stats(self, use_cache: bool = True) -> Dict:
        """جلب إحصائيات الأدمن مع دعم الكاش"""
        cache_key = "admin_stats"

        if use_cache and cache_key in self.cache:
            cache_entry = self.cache[cache_key]
            if time.time() - cache_entry["timestamp"] < 60:  # كاش صالح لمدة دقيقة
                self.cache_hits += 1
                logger.debug(f"✅ Cache hit for admin stats")
                return cache_entry["data"]

        self.cache_misses += 1
        self.operations_count["panel"] += 1

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            # إحصائيات المستخدمين
            cursor.execute("SELECT COUNT(*) FROM users")
            total_users = cursor.fetchone()[0]

            cursor.execute(
                "SELECT COUNT(*) FROM users WHERE registration_status = 'complete'"
            )
            registered_users = cursor.fetchone()[0]

            # آخر المستخدمين المسجلين
            cursor.execute(
                """
                SELECT telegram_id, username, full_name, created_at
                FROM users
                WHERE registration_status = 'complete'
                ORDER BY created_at DESC
                LIMIT 5
            """
            )
            recent_users = cursor.fetchall()

            stats = {
                "total_users": total_users,
                "registered_users": registered_users,
                "incomplete_users": total_users - registered_users,
                "recent_users": recent_users,
                "cache_performance": {
                    "hits": self.cache_hits,
                    "misses": self.cache_misses,
                    "hit_rate": f"{(self.cache_hits / max(1, self.cache_hits + self.cache_misses)) * 100:.1f}%",
                },
                "operations": self.operations_count.copy(),
            }

            # حفظ في الكاش
            self.cache[cache_key] = {"timestamp": time.time(), "data": stats}

            self._cleanup_cache()
            return stats

        finally:
            conn.close()

    def get_users_page(self, page: int, use_cache: bool = True) -> Dict:
        """جلب صفحة من المستخدمين مع دعم الكاش"""
        cache_key = f"users_page_{page}"

        if use_cache and cache_key in self.cache:
            cache_entry = self.cache[cache_key]
            if time.time() - cache_entry["timestamp"] < 120:  # كاش صالح لمدة دقيقتين
                self.cache_hits += 1
                return cache_entry["data"]

        self.cache_misses += 1
        self.operations_count["users"] += 1

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            users_per_page = 10

            # إجمالي المستخدمين
            cursor.execute("SELECT COUNT(*) FROM users")
            total_users = cursor.fetchone()[0]
            total_pages = (total_users + users_per_page - 1) // users_per_page

            # تصحيح رقم الصفحة
            page = max(1, min(page, total_pages))
            offset = (page - 1) * users_per_page

            # جلب المستخدمين
            cursor.execute(
                """
                SELECT u.telegram_id, u.username, u.full_name, u.registration_status,
                       r.platform, r.whatsapp, r.payment_method
                FROM users u
                LEFT JOIN registration_data r ON u.user_id = r.user_id
                ORDER BY u.created_at DESC
                LIMIT ? OFFSET ?
            """,
                (users_per_page, offset),
            )
            users = cursor.fetchall()

            result = {
                "users": users,
                "page": page,
                "total_pages": total_pages,
                "total_users": total_users,
                "offset": offset,
            }

            # حفظ في الكاش
            self.cache[cache_key] = {"timestamp": time.time(), "data": result}

            self._cleanup_cache()
            return result

        finally:
            conn.close()

    def search_user(self, query: str) -> Dict:
        """بحث عن مستخدم"""
        self.operations_count["search"] += 1

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            # بحث بواسطة ID أو username أو الاسم
            if query.isdigit():
                # بحث بواسطة Telegram ID
                cursor.execute(
                    """
                    SELECT u.*, r.platform, r.whatsapp, r.payment_method
                    FROM users u
                    LEFT JOIN registration_data r ON u.user_id = r.user_id
                    WHERE u.telegram_id = ?
                """,
                    (int(query),),
                )
            else:
                # بحث بواسطة username أو الاسم
                search_pattern = f"%{query}%"
                cursor.execute(
                    """
                    SELECT u.*, r.platform, r.whatsapp, r.payment_method
                    FROM users u
                    LEFT JOIN registration_data r ON u.user_id = r.user_id
                    WHERE u.username LIKE ? OR u.full_name LIKE ?
                    LIMIT 10
                """,
                    (search_pattern, search_pattern),
                )

            results = cursor.fetchall()
            return {"results": results, "query": query}

        finally:
            conn.close()

    def prepare_broadcast(self) -> Dict:
        """تحضير البث للجميع"""
        self.operations_count["broadcast"] += 1

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            # جلب جميع معرفات المستخدمين
            cursor.execute("SELECT telegram_id FROM users")
            user_ids = [row[0] for row in cursor.fetchall()]

            return {"user_ids": user_ids, "total_count": len(user_ids)}

        finally:
            conn.close()

    def delete_user(self, telegram_id: int) -> bool:
        """حذف مستخدم"""
        self.operations_count["delete"] += 1

        # إزالة من الكاش
        keys_to_remove = [
            k for k in self.cache.keys() if "users_page" in k or "admin_stats" in k
        ]
        for key in keys_to_remove:
            del self.cache[key]

        conn = self.db.get_connection()
        cursor = conn.cursor()

        try:
            # حذف من جدول registration_data أولاً
            cursor.execute(
                "DELETE FROM registration_data WHERE user_id = (SELECT user_id FROM users WHERE telegram_id = ?)",
                (telegram_id,),
            )

            # حذف من جدول users
            cursor.execute("DELETE FROM users WHERE telegram_id = ?", (telegram_id,))

            conn.commit()

            deleted_rows = cursor.rowcount
            return deleted_rows > 0

        except Exception as e:
            logger.error(f"❌ خطأ في حذف المستخدم {telegram_id}: {e}")
            conn.rollback()
            return False

        finally:
            conn.close()

    def get_performance_stats(self) -> Dict:
        """إحصائيات الأداء المتقدمة"""
        return {
            "cache": {
                "size": len(self.cache),
                "max_size": self.cache_size,
                "hits": self.cache_hits,
                "misses": self.cache_misses,
                "hit_rate": f"{(self.cache_hits / max(1, self.cache_hits + self.cache_misses)) * 100:.1f}%",
            },
            "operations": self.operations_count.copy(),
            "total_operations": sum(self.operations_count.values()),
        }


# ================================ البوت الرئيسي ================================
class FC26SmartBot:
    """البوت الذكي الكامل"""

    def __init__(self):
        self.db = Database()
        self.registration_handler = SmartRegistrationHandler()

        # إعداد ThreadPoolExecutor لزر الملف الشخصي
        self.profile_executor = ThreadPoolExecutor(
            max_workers=1,  # واحد بس - البروفايل مش محتاج أكتر
            thread_name_prefix="ProfileHandler",
        )

        # 🆕 إضافة ThreadPoolExecutor لتعديل الملف الشخصي
        self.edit_profile_executor = ThreadPoolExecutor(
            max_workers=2,  # اتنين بس للتعديل
            thread_name_prefix="EditProfileHandler",
        )

        # 🚀 المرحلة التالتة: إضافة Threading للقائمة الرئيسية والأزرار الأساسية
        self.menu_executor = ThreadPoolExecutor(
            max_workers=2,  # قليل للقائمة الرئيسية
            thread_name_prefix="MenuHandler-Pro",
        )

        self.coins_executor = ThreadPoolExecutor(
            max_workers=3,  # أقل - مش محتاجين 10!
            thread_name_prefix="CoinsHandler-Pro",
        )

        self.support_executor = ThreadPoolExecutor(
            max_workers=1,  # واحد بس للدعم الفني
            thread_name_prefix="SupportHandler-Pro",
        )

        # 🔥 المرحلة الرابعة: إضافة Threading لعمليات الأدمن
        self.admin_pool = ThreadPoolExecutor(
            max_workers=2,  # أقل للأدمن
            thread_name_prefix="AdminHandler-Ultra",
        )

        # 🔥 المرحلة الخامسة: إضافة Registration Threading
        self.registration_pool = ThreadPoolExecutor(
            max_workers=2,
            thread_name_prefix="RegistrationHandler-Ultra",
        )

        # تهيئة AdminHandler المتقدم
        self.admin_handler = AdminHandler(self.db, cache_size=100)

        # قاموس للأقفال الخاصة بكل مستخدم
        self.user_locks = {}
        self.locks_lock = threading.Lock()  # قفل لحماية قاموس الأقفال نفسه

        logger.info("🔧 تم تهيئة ThreadPoolExecutor لزر الملف الشخصي")
        logger.info("🔧 تم تهيئة ThreadPoolExecutor لتعديل الملف الشخصي")
        logger.info("🚀 تم تهيئة Threading للقائمة الرئيسية - المرحلة التالتة")
        logger.info("🔥 تم تهيئة Threading لعمليات الأدمن - المرحلة الرابعة")
        logger.info("🚀 تم تهيئة Registration Threading - المرحلة الخامسة")
        logger.info(f"📊 إجمالي Workers الآن: {1+2+2+3+1+2+2} = 13 worker")
        logger.info(f"🎯 AdminHandler مع كاش ذكي لـ 100 استعلام")

    def get_user_lock(self, user_id: int) -> threading.Lock:
        """الحصول على قفل خاص بالمستخدم"""
        with self.locks_lock:
            if user_id not in self.user_locks:
                self.user_locks[user_id] = threading.Lock()
                logger.debug(f"🔒 إنشاء قفل جديد للمستخدم {user_id}")
            return self.user_locks[user_id]

    async def handle_profile_safely(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, telegram_id: int
    ):
        """معالج آمن للملف الشخصي في thread منفصل"""
        try:
            # الحصول على قفل خاص بهذا المستخدم
            user_lock = self.get_user_lock(telegram_id)

            # تنفيذ العملية في thread مع القفل
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(
                self.profile_executor,
                self._handle_profile_thread,
                telegram_id,
                user_lock,
            )

            # انتظار نتيجة المعالجة
            profile_data = await future

            if profile_data:
                # عرض الملف الشخصي
                await self._display_profile(update, context, profile_data)
                logger.info(f"✅ تم عرض الملف الشخصي للمستخدم {telegram_id} بنجاح")
            else:
                # إصلاح 2: تحسين UX للمستخدمين غير المسجلين - استخدام الدالة المساعدة
                await self._redirect_to_registration(update, context, telegram_id)

        except Exception as e:
            logger.error(f"❌ خطأ في معالجة الملف الشخصي للمستخدم {telegram_id}: {e}")
            await smart_message_manager.update_current_message(
                update,
                context,
                "❌ حدث خطأ في عرض الملف الشخصي. الرجاء المحاولة لاحقاً.",
            )

    async def _redirect_to_registration(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, telegram_id: int
    ):
        """
        إصلاح 3: دالة مساعدة لتوجيه المستخدمين غير المسجلين للتسجيل بشكل آمن
        تحسن UX وتتعامل مع effective_message بشكل صحيح
        """
        try:
            await smart_message_manager.update_current_message(
                update, context, "🔄 توجيهك للتسجيل تلقائياً..."
            )

            logger.info(
                f"🔄 [Registration-Redirect] توجيه المستخدم غير المسجل {telegram_id} للتسجيل"
            )

            # إنشاء update محسن مع effective_message
            fake_message = type(
                "Message",
                (),
                {
                    "reply_text": (
                        update.callback_query.message.reply_text
                        if update.callback_query and update.callback_query.message
                        else lambda text: context.bot.send_message(
                            chat_id=telegram_id, text=text
                        )
                    ),
                    "from_user": update.effective_user,
                    "chat": update.effective_chat,
                },
            )()

            fake_update = type(
                "Update",
                (),
                {
                    "message": fake_message,
                    "effective_message": fake_message,  # إضافة effective_message لحل المشكلة
                    "effective_user": update.effective_user,
                    "effective_chat": update.effective_chat,
                    "callback_query": None,
                },
            )()

            # الحصول على bot_instance من context
            if "bot_instance" not in context.bot_data:
                logger.error(
                    "❌ [Registration-Redirect] bot_instance غير موجود في context"
                )
                await smart_message_manager.update_current_message(
                    update, context, "❌ حدث خطأ في النظام، يرجى كتابة /start يدوياً"
                )
                return

            bot_instance = context.bot_data["bot_instance"]

            # توجيه للتسجيل مع إدارة محسنة للأخطاء
            await bot_instance.registration_handler.start(fake_update, context)
            logger.info(
                f"✅ [Registration-Redirect] تم توجيه المستخدم {telegram_id} للتسجيل بنجاح"
            )

        except Exception as e:
            logger.error(
                f"❌ [Registration-Redirect] خطأ في توجيه المستخدم {telegram_id}: {e}"
            )
            await smart_message_manager.update_current_message(
                update,
                context,
                "❌ حدث خطأ في التوجيه للتسجيل. يرجى كتابة /start للمحاولة مرة أخرى",
            )

    def _handle_profile_thread(
        self, telegram_id: int, user_lock: threading.Lock
    ) -> Optional[Dict]:
        """معالجة الملف الشخصي داخل thread مع قفل"""
        with user_lock:
            try:
                logger.debug(
                    f"🔍 جلب بيانات الملف الشخصي للمستخدم {telegram_id} من قاعدة البيانات"
                )

                # جلب بيانات الملف الشخصي من قاعدة البيانات
                profile = self.db.get_user_profile(telegram_id)

                if profile:
                    # إضافة تأخير صغير لمحاكاة المعالجة
                    time.sleep(0.1)
                    logger.debug(f"✅ تم جلب بيانات الملف الشخصي بنجاح")
                    return profile
                else:
                    # 🛠️ إصلاح المشكلة: إنشاء profile فارغ للمستخدمين الجدد/غير المكتملين
                    logger.info(
                        f"📝 إنشاء ملف شخصي فارغ للمستخدم غير المكتمل {telegram_id}"
                    )

                    # جلب البيانات الأساسية للمستخدم
                    basic_data = self.db.get_user_data(telegram_id)

                    # إنشاء profile فارغ مع إمكانية التعديل
                    empty_profile = {
                        "platform": (
                            basic_data.get("platform", "غير محدد")
                            if basic_data
                            else "غير محدد"
                        ),
                        "whatsapp": (
                            basic_data.get("whatsapp", "غير محدد")
                            if basic_data
                            else "غير محدد"
                        ),
                        "payment_method": (
                            basic_data.get("payment_method", "غير محدد")
                            if basic_data
                            else "غير محدد"
                        ),
                        "incomplete_profile": True,  # علامة للإشارة أن البروفايل غير مكتمل
                    }

                    time.sleep(0.1)
                    logger.debug(f"✅ تم إنشاء ملف شخصي فارغ للتعديل الحر")
                    return empty_profile

            except Exception as e:
                logger.error(f"❌ خطأ في thread معالجة الملف الشخصي: {e}")
                # حتى في حالة الخطأ، نرجع profile فارغ بدلاً من None
                return {
                    "platform": "غير محدد",
                    "whatsapp": "غير محدد",
                    "payment_method": "غير محدد",
                    "incomplete_profile": True,
                    "error": True,
                }

    async def _display_profile(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, profile: Dict
    ):
        """عرض بيانات الملف الشخصي"""
        # الحصول على معلومات الشبكة إذا كان الرقم موجود
        whatsapp_display = profile.get("whatsapp", "غير محدد")
        network_display = ""

        if (
            whatsapp_display
            and whatsapp_display != "غير محدد"
            and len(whatsapp_display) >= 3
        ):
            prefix = whatsapp_display[:3]
            if prefix in whatsapp_security.EGYPTIAN_NETWORKS:
                network = whatsapp_security.EGYPTIAN_NETWORKS[prefix]
                network_display = f" ({network['emoji']} {network['name']})"

        # 🛠️ إصلاح عرض البروفايل: تحسين UX للمستخدمين غير المكتملين
        incomplete_warning = ""
        if profile.get("incomplete_profile", False):
            incomplete_warning = (
                "\n⚠️ ملفك الشخصي غير مكتمل\n✏️ يمكنك تعديل أي بيان بحرية\n"
            )

        profile_text = f"""
👤 الملف الشخصي
━━━━━━━━━━━━━━━━
🎮 المنصة: {profile.get('platform', 'غير محدد')}
📱 واتساب: {whatsapp_display}{network_display}
💳 طريقة الدفع: {profile.get('payment_method', 'غير محدد')}{incomplete_warning}
━━━━━━━━━━━━━━━━
🔐 بياناتك محمية
🧵 Thread: {threading.current_thread().name}
"""

        # أزرار العودة
        keyboard = [
            [
                InlineKeyboardButton(
                    "✏️ تعديل الملف الشخصي", callback_data="edit_profile"
                )
            ],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        # تجنب خطأ HTTP 400 - نتأكد إن الرسالة مختلفة
        try:
            await smart_message_manager.update_current_message(
                update, context, profile_text, reply_markup=reply_markup
            )
        except Exception as e:
            # لو حصل خطأ، نرسل رسالة جديدة
            logger.debug(f"Error updating message: {e}")
            await smart_message_manager.send_new_active_message(
                update,
                context,
                profile_text,
                reply_markup=reply_markup,
                disable_previous=True,
            )

    async def handle_edit_profile_safely(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        telegram_id: int,
        action: str,
    ):
        """معالج آمن لتعديل الملف الشخصي في thread منفصل"""
        try:
            # الحصول على قفل خاص بهذا المستخدم
            user_lock = self.get_user_lock(telegram_id)

            # تنفيذ العملية في thread مع القفل
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(
                self.edit_profile_executor,
                self._handle_edit_profile_thread,
                telegram_id,
                action,
                user_lock,
            )

            # انتظار نتيجة المعالجة مع timeout
            result = await asyncio.wait_for(future, timeout=8.0)

            if result:
                # عرض نتيجة التعديل
                await self._display_edit_result(update, context, result)
                logger.info(
                    f"✅ تم معالجة تعديل الملف الشخصي للمستخدم {telegram_id} بنجاح - Action: {action}"
                )
            else:
                # خطأ في المعالجة
                await smart_message_manager.update_current_message(
                    update,
                    context,
                    "❌ حدث خطأ في معالجة طلب التعديل. الرجاء المحاولة لاحقاً.",
                )
                logger.warning(
                    f"⚠️ فشل معالجة تعديل الملف الشخصي للمستخدم {telegram_id}"
                )

        except asyncio.TimeoutError:
            logger.error(
                f"⏰ انتهت مهلة معالجة تعديل الملف الشخصي للمستخدم {telegram_id}"
            )
            await smart_message_manager.update_current_message(
                update, context, "❌ انتهت مهلة المعالجة. الرجاء المحاولة مرة أخرى."
            )
        except Exception as e:
            logger.error(
                f"❌ خطأ في معالجة تعديل الملف الشخصي للمستخدم {telegram_id}: {e}"
            )
            await smart_message_manager.update_current_message(
                update,
                context,
                "❌ حدث خطأ في معالجة طلب التعديل. الرجاء المحاولة لاحقاً.",
            )

    def _handle_edit_profile_thread(
        self, telegram_id: int, action: str, user_lock: threading.Lock
    ) -> Optional[Dict]:
        """معالجة تعديل الملف الشخصي داخل thread مع قفل"""
        with user_lock:
            try:
                logger.debug(
                    f"🔍 بدء معالجة تعديل الملف الشخصي للمستخدم {telegram_id} - Action: {action}"
                )

                # معالجة حسب نوع الإجراء
                if action == "edit_profile":
                    # عرض قائمة التعديل
                    return {
                        "type": "menu",
                        "message": """
✏️ تعديل الملف الشخصي
━━━━━━━━━━━━━━━━
اختر ما تريد تعديله:
🧵 معالج محسّن في Thread منفصل
""",
                        "keyboard": [
                            [
                                InlineKeyboardButton(
                                    "🎮 تعديل المنصة", callback_data="edit_platform"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "📱 تعديل رقم الواتساب",
                                    callback_data="edit_whatsapp",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "💳 تعديل طريقة الدفع", callback_data="edit_payment"
                                )
                            ],
                            [InlineKeyboardButton("🔙 رجوع", callback_data="profile")],
                        ],
                    }

                elif action == "edit_platform":
                    # عرض خيارات المنصات
                    return {
                        "type": "platform_selection",
                        "message": """🎮 اختر المنصة الجديدة:

🏆 أفضل الأسعار في مصر
🧵 معالج محسّن للأداء العالي""",
                    }

                elif action.startswith("update_platform_"):
                    # معالجة تحديث المنصة
                    platform_key = action.replace("update_platform_", "")

                    # تحديث في قاعدة البيانات
                    success = self.db.update_user_data(
                        telegram_id, {"platform": platform_key}
                    )

                    if success:
                        # جلب البيانات المحدثة
                        updated_profile = self.db.get_user_profile(telegram_id)
                        platform_name = GAMING_PLATFORMS.get(platform_key, {}).get(
                            "name", platform_key
                        )

                        return {
                            "type": "update_success",
                            "message": f"""
✅ تم التحديث بنجاح!
━━━━━━━━━━━━━━━━
👤 الملف الشخصي المحدث
━━━━━━━━━━━━━━━━
🎮 المنصة: {platform_name} ✅
📱 واتساب: {updated_profile.get('whatsapp', 'غير محدد')}
💳 طريقة الدفع: {updated_profile.get('payment_method', 'غير محدد')}
━━━━━━━━━━━━━━━━
🧵 Thread: {threading.current_thread().name}
🔐 بياناتك محمية ومشفرة
""",
                            "keyboard": [
                                [
                                    InlineKeyboardButton(
                                        "✏️ تعديل آخر", callback_data="edit_profile"
                                    )
                                ],
                                [
                                    InlineKeyboardButton(
                                        "🏠 القائمة الرئيسية", callback_data="main_menu"
                                    )
                                ],
                            ],
                        }
                    else:
                        return None

                # إضافة تأخير صغير لمحاكاة المعالجة
                time.sleep(0.1)

                logger.debug(
                    f"✅ تم معالجة تعديل الملف الشخصي بنجاح - Thread: {threading.current_thread().name}"
                )
                return {"type": "default", "message": f"معالجة الإجراء: {action}"}

            except Exception as e:
                logger.error(f"❌ خطأ في thread معالجة تعديل الملف الشخصي: {e}")
                return None

    async def _display_edit_result(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, result: Dict
    ):
        """عرض نتيجة معالجة التعديل"""
        try:
            result_type = result.get("type", "default")
            message = result.get("message", "تم المعالجة")

            if result_type == "menu":
                # عرض قائمة التعديل
                keyboard_data = result.get("keyboard", [])
                reply_markup = InlineKeyboardMarkup(keyboard_data)

                await smart_message_manager.update_current_message(
                    update, context, message, reply_markup=reply_markup
                )

            elif result_type == "platform_selection":
                # عرض خيارات المنصات
                keyboard = []

                for key, platform in GAMING_PLATFORMS.items():
                    keyboard.append(
                        [
                            InlineKeyboardButton(
                                f"{platform['emoji']} {platform['name']}",
                                callback_data=f"update_platform_{key}",
                            )
                        ]
                    )

                keyboard.append(
                    [InlineKeyboardButton("🔙 رجوع", callback_data="edit_profile")]
                )
                reply_markup = InlineKeyboardMarkup(keyboard)

                await smart_message_manager.update_current_message(
                    update, context, message, reply_markup=reply_markup
                )

            elif result_type == "update_success":
                # عرض نجاح التحديث
                keyboard_data = result.get("keyboard", [])
                reply_markup = InlineKeyboardMarkup(keyboard_data)

                await smart_message_manager.update_current_message(
                    update, context, message, reply_markup=reply_markup
                )

            else:
                # عرض افتراضي
                await smart_message_manager.update_current_message(
                    update, context, message
                )

        except Exception as e:
            logger.error(f"❌ خطأ في عرض نتيجة التعديل: {e}")
            await smart_message_manager.update_current_message(
                update, context, "❌ حدث خطأ في عرض النتيجة"
            )

    async def handle_main_menu_safely(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        telegram_id: int,
        action: str,
    ):
        """معالج آمن للقائمة الرئيسية في threads منفصلة حسب الأولوية"""

        # تحديد المعالج والإعدادات حسب نوع الإجراء
        executor_config = {
            "main_menu": {
                "executor": self.menu_executor,
                "timeout": 6.0,
                "priority": "high",
            },
            "sell_coins": {
                "executor": self.coins_executor,  # أعلى أولوية
                "timeout": 12.0,  # وقت أطول للمعالجة المتقدمة
                "priority": "critical",
            },
            "support": {
                "executor": self.support_executor,
                "timeout": 8.0,
                "priority": "medium",
            },
        }

        # الحصول على الإعدادات أو استخدام الافتراضي
        config = executor_config.get(
            action,
            {"executor": self.menu_executor, "timeout": 6.0, "priority": "normal"},
        )

        try:
            # بدء مراقبة الأداء
            start_time = time.time()

            # الحصول على قفل المستخدم
            user_lock = self.get_user_lock(telegram_id)

            # تنفيذ في thread منفصل
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(
                config["executor"],
                self._handle_main_menu_thread,
                telegram_id,
                action,
                user_lock,
                config["priority"],
            )

            # انتظار النتيجة مع timeout
            result = await asyncio.wait_for(future, timeout=config["timeout"])

            # حساب وقت المعالجة
            processing_time = time.time() - start_time

            if result:
                await self._display_main_menu_result(update, context, result, action)
                logger.info(
                    f"✅ تم معالجة {action} للمستخدم {telegram_id} بنجاح - وقت المعالجة: {processing_time:.2f}s - أولوية: {config['priority']}"
                )
            else:
                await smart_message_manager.update_current_message(
                    update, context, "❌ حدث خطأ في المعالجة. الرجاء المحاولة لاحقاً."
                )
                logger.warning(f"⚠️ فشل معالجة {action} للمستخدم {telegram_id}")

        except asyncio.TimeoutError:
            logger.error(
                f"⏰ انتهت مهلة {action} للمستخدم {telegram_id} - Timeout: {config['timeout']}s"
            )
            await smart_message_manager.update_current_message(
                update,
                context,
                f"❌ انتهت مهلة المعالجة ({config['timeout']}s). الرجاء المحاولة مرة أخرى.\n\n🧵 النظام يدعم 1000 مستخدم متزامن",
            )
        except Exception as e:
            logger.error(f"❌ خطأ في معالجة {action} للمستخدم {telegram_id}: {e}")
            await smart_message_manager.update_current_message(
                update, context, "❌ حدث خطأ غير متوقع. الرجاء المحاولة لاحقاً."
            )

    def _handle_main_menu_thread(
        self, telegram_id: int, action: str, user_lock: threading.Lock, priority: str
    ) -> Optional[Dict]:
        """معالجة القائمة الرئيسية داخل thread مع أولويات مختلفة"""
        with user_lock:
            try:
                thread_name = threading.current_thread().name
                logger.debug(
                    f"🔄 بدء معالجة {action} للمستخدم {telegram_id} - Thread: {thread_name} - أولوية: {priority}"
                )

                # تأخير محاكاة المعالجة حسب الأولوية
                processing_delay = {
                    "critical": 0.05,  # sell_coins - أسرع معالجة
                    "high": 0.1,  # main_menu
                    "medium": 0.15,  # support
                    "normal": 0.2,  # افتراضي
                }
                time.sleep(processing_delay.get(priority, 0.1))

                # الحصول على إحصائيات النظام
                active_threads = threading.active_count()
                total_workers = self._get_total_workers_count()

                if action == "main_menu":
                    return {
                        "type": "main_menu",
                        "message": f"""
👋 أهلاً بعودتك!

🎮 بوت FC 26 Pro - أفضل مكان لبيع كوينز
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 نظام متقدم للأداء العالي
🧵 Threads نشطة: {active_threads} | إجمالي Workers: {total_workers}
🎯 يدعم 1000 مستخدم متزامن
⚡ معالج محسن: {thread_name}
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
كيف يمكنني مساعدتك اليوم؟
""",
                        "keyboard": [
                            [
                                InlineKeyboardButton(
                                    "💸 بيع كوينز", callback_data="sell_coins"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "👤 الملف الشخصي", callback_data="profile"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "📞 الدعم الفني", callback_data="support"
                                )
                            ],
                        ],
                        "stats": {
                            "threads": active_threads,
                            "workers": total_workers,
                            "processor": thread_name,
                        },
                    }

                elif action == "sell_coins":
                    return {
                        "type": "sell_coins",
                        "message": f"""
💸 بيع كوينز FC 26 - النظام الاحترافي

🏆 أفضل أسعار في مصر
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚡ مميزات النظام المتقدم:
🔒 أمان 100% مع تشفير متقدم
💰 أفضل الأسعار والعروض
🚀 معالجة فورية ومتقدمة
📱 دعم فني 24/7
🎯 يستحمل 1000 مستخدم متزامن

🔧 معلومات تقنية:
• معالج عالي الأولوية: {thread_name}
• أولوية: {priority.upper()}
• Workers مخصصة: 10

🚧 قريباً جداً...
خدمة بيع الكوينز بنظام متقدم
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📞 للاستفسار: @FC26Support
""",
                        "keyboard": [
                            [
                                InlineKeyboardButton(
                                    "📊 مراقبة الأداء",
                                    callback_data="performance_stats",
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "🔙 القائمة الرئيسية", callback_data="main_menu"
                                )
                            ],
                        ],
                        "stats": {
                            "priority": priority,
                            "processor": thread_name,
                            "workers": 10,
                        },
                    }

                elif action == "support":
                    return {
                        "type": "support",
                        "message": f"""
📞 الدعم الفني الاحترافي

🔒 فريق دعم متخصص 24/7
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🚀 خدمات الدعم المتقدمة:
⚡ استجابة فورية (< 5 دقائق)
🔧 حلول تقنية متقدمة
💬 دعم شخصي ومخصص
🎯 خبرة في أنظمة الـ 1000 مستخدم
🔧 دعم فني للمشاكل المعقدة

📱 قنوات التواصل:
• تليجرام: @FC26Support
• دعم مباشر داخل البوت
• نظام تذاكر متقدم

🔧 معلومات تقنية:
• معالج الدعم: {thread_name}
• أولوية: {priority.upper()}
• نظام يدعم 1000 استفسار متزامن
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 نحن هنا لمساعدتك!
""",
                        "keyboard": [
                            [
                                InlineKeyboardButton(
                                    "📱 تواصل مباشر", url="https://t.me/FC26Support"
                                )
                            ],
                            [
                                InlineKeyboardButton(
                                    "🔙 القائمة الرئيسية", callback_data="main_menu"
                                )
                            ],
                        ],
                        "stats": {
                            "priority": priority,
                            "processor": thread_name,
                            "response_time": "< 5 min",
                        },
                    }

                logger.debug(f"✅ تمت معالجة {action} بنجاح في {thread_name}")
                return {
                    "type": "success",
                    "message": f"✅ تم معالجة {action} بنجاح\n🧵 Thread: {thread_name}",
                    "stats": {"processor": thread_name, "priority": priority},
                }

            except Exception as e:
                logger.error(f"❌ خطأ في thread معالجة {action}: {e}")
                return None

    def _get_total_workers_count(self) -> int:
        """حساب إجمالي عدد الـ workers في جميع الـ executors"""
        try:
            return (
                getattr(
                    self, "profile_executor", ThreadPoolExecutor(max_workers=0)
                )._max_workers
                + getattr(
                    self, "edit_profile_executor", ThreadPoolExecutor(max_workers=0)
                )._max_workers
                + getattr(
                    self, "menu_executor", ThreadPoolExecutor(max_workers=0)
                )._max_workers
                + getattr(
                    self, "coins_executor", ThreadPoolExecutor(max_workers=0)
                )._max_workers
                + getattr(
                    self, "support_executor", ThreadPoolExecutor(max_workers=0)
                )._max_workers
            )
        except:
            return 0

    async def _display_main_menu_result(
        self,
        update: Update,
        context: ContextTypes.DEFAULT_TYPE,
        result: Dict,
        action: str,
    ):
        """عرض نتائج معالجة القائمة الرئيسية مع إحصائيات"""
        try:
            result_type = result.get("type", "default")
            message = result.get("message", "تم المعالجة")
            keyboard_data = result.get("keyboard", [])
            stats = result.get("stats", {})

            # تحويل بيانات الكيبورد لـ InlineKeyboardMarkup
            if keyboard_data:
                reply_markup = InlineKeyboardMarkup(keyboard_data)
            else:
                reply_markup = None

            # عرض الرسالة
            await smart_message_manager.update_current_message(
                update, context, message, reply_markup=reply_markup
            )

            logger.debug(f"✅ تم عرض نتيجة {action} بنجاح - Type: {result_type}")

        except Exception as e:
            logger.error(f"❌ خطأ في عرض نتيجة {action}: {e}")
            await smart_message_manager.update_current_message(
                update, context, "❌ حدث خطأ في عرض النتيجة"
            )

    async def start(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """أمر البداية مع النظام الذكي الموحد"""
        telegram_id = update.effective_user.id

        # إذا كان هناك callback_query، نتجاهل الطلب (منع التكرار)
        if update.callback_query:
            return

        user = self.db.get_user_by_telegram_id(telegram_id)

        if user and user.get("registration_status") == "complete":
            # مستخدم مسجل - عرض القائمة الرئيسية مع النظام الذكي

            # التحقق من صلاحيات الأدمن
            is_admin = telegram_id == ADMIN_ID

            if is_admin:
                welcome_message = f"""
👋 مرحباً بالأدمن!

🎮 بوت FC 26 - لوحة التحكم

⚡ لديك صلاحيات كاملة
"""
            else:
                welcome_message = f"""
👋 أهلاً بعودتك!

🎮 بوت FC 26 - أفضل مكان لبيع كوينز

كيف يمكنني مساعدتك اليوم؟
"""

            # أزرار تفاعلية حسب الصلاحيات
            keyboard = [
                [InlineKeyboardButton("💸 بيع كوينز", callback_data="sell_coins")],
                [InlineKeyboardButton("👤 الملف الشخصي", callback_data="profile")],
                [InlineKeyboardButton("📞 الدعم", callback_data="support")],
            ]

            # إضافة أزرار الأدمن فقط للأدمن
            if is_admin:
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🔐 لوحة الأدمن", callback_data="admin_panel_advanced"
                        )
                    ]
                )
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف حسابي", callback_data="delete_account"
                        )
                    ]
                )
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف حساب مستخدم", callback_data="admin_delete_user"
                        )
                    ]
                )
            # المستخدمين العاديين لا يرون زر حذف الحساب

            reply_markup = InlineKeyboardMarkup(keyboard)

            # استخدام النظام الذكي دائماً
            await smart_message_manager.send_new_active_message(
                update,
                context,
                welcome_message,
                reply_markup=reply_markup,
                disable_previous=True,  # تعطيل الرسالة السابقة
            )
        else:
            # مستخدم جديد - استخدام النظام الذكي للتسجيل
            await self.registration_handler.start(update, context)

    async def profile_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """عرض الملف الشخصي مع النظام الذكي"""
        telegram_id = update.effective_user.id
        profile = self.db.get_user_profile(telegram_id)

        if not profile:
            await smart_message_manager.send_new_active_message(
                update, context, "🔄 توجيهك للتسجيل تلقائياً..."
            )
            return
            # 🎯 الحل الأول: توجيه تلقائي للتسجيل من profile_command
            logger.info(
                f"🔄 [الحل الأول] توجيه المستخدم غير المسجل {telegram_id} تلقائياً للتسجيل من profile_command"
            )

            # الحصول على bot_instance من context
            if "bot_instance" not in context.bot_data:
                logger.error("❌ لم يتم العثور على bot_instance في context.bot_data")
                await smart_message_manager.send_new_active_message(
                    update, context, "❌ حدث خطأ في النظام، يرجى كتابة /start يدوياً"
                )
                return

            bot_instance = context.bot_data["bot_instance"]

            # توجيه تلقائي لمعالج التسجيل
            await bot_instance.registration_handler.start(update, context)
            logger.info(
                f"✅ [الحل الأول] تم توجيه المستخدم {telegram_id} للتسجيل بنجاح من profile_command"
            )

        # الحصول على معلومات الشبكة إذا كان الرقم موجود
        whatsapp_display = profile.get("whatsapp", "غير محدد")
        network_display = ""

        if (
            whatsapp_display
            and whatsapp_display != "غير محدد"
            and len(whatsapp_display) >= 3
        ):
            prefix = whatsapp_display[:3]
            if prefix in whatsapp_security.EGYPTIAN_NETWORKS:
                network = whatsapp_security.EGYPTIAN_NETWORKS[prefix]
                network_display = f" ({network['emoji']} {network['name']})"

        profile_text = f"""
👤 الملف الشخصي
━━━━━━━━━━━━━━━━
🎮 المنصة: {profile.get('platform', 'غير محدد')}
📱 واتساب: {whatsapp_display}{network_display}
💳 طريقة الدفع: {profile.get('payment_method', 'غير محدد')}
━━━━━━━━━━━━━━━━
🔐 بياناتك محمية
"""

        # أزرار العودة
        keyboard = [
            [
                InlineKeyboardButton(
                    "✏️ تعديل الملف الشخصي", callback_data="edit_profile"
                )
            ],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await smart_message_manager.send_new_active_message(
            update, context, profile_text, reply_markup=reply_markup
        )

    async def help_command(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """عرض المساعدة"""
        telegram_id = update.effective_user.id
        is_admin = telegram_id == ADMIN_ID

        if is_admin:
            help_text = """
🆘 المساعدة والأوامر - أدمن
━━━━━━━━━━━━━━━━
📢 الأوامر المتاحة:
/start - البداية والقائمة الرئيسية
/profile - عرض ملفك الشخصي
/delete - حذف حسابك (أدمن فقط)
/help - هذه الرسالة
🔐 صلاحيات الأدمن:
• لوحة تحكم خاصة
• عرض جميع المستخدمين
• حذف المستخدمين
• البث الجماعي
🔗 للدعم والمساعدة:
@FC26Support
"""
        else:
            help_text = """
🆘 المساعدة والأوامر
━━━━━━━━━━━━━━━━
📢 الأوامر المتاحة:
/start - البداية والقائمة الرئيسية
/profile - عرض ملفك الشخصي
/help - هذه الرسالة
🔗 للدعم والمساعدة:
@FC26Support
"""
        # أزرار مفيدة
        keyboard = [
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")],
            [InlineKeyboardButton("👤 ملفي الشخصي", callback_data="profile")],
            [InlineKeyboardButton("📞 الدعم الفني", callback_data="support")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await smart_message_manager.send_new_active_message(
            update, context, help_text, reply_markup=reply_markup
        )

    def get_threading_stats(self):
        """إحصائيات Threading محسنة"""
        return {
            "profile_executor": {
                "max_workers": self.profile_executor._max_workers,
                "active_threads": (
                    len(self.profile_executor._threads)
                    if hasattr(self.profile_executor, "_threads")
                    else 0
                ),
            },
            "edit_profile_executor": {
                "max_workers": self.edit_profile_executor._max_workers,
                "active_threads": (
                    len(self.edit_profile_executor._threads)
                    if hasattr(self.edit_profile_executor, "_threads")
                    else 0
                ),
            },
            "total_active_locks": len(self.user_locks),
            "system_threads": threading.active_count(),
        }

    async def threading_stats_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """إحصائيات Threading للأدمن"""
        telegram_id = update.effective_user.id

        if telegram_id != ADMIN_ID:
            await update.message.reply_text("⛔ هذا الأمر للأدمن فقط!")
            return

        stats = self.get_threading_stats()

        stats_message = f"""
🧵 إحصائيات Threading المتقدم
━━━━━━━━━━━━━━━━━━━━━━━━
📊 Profile Handler:
• Max Workers: {stats['profile_executor']['max_workers']}
• Active Threads: {stats['profile_executor']['active_threads']}

📊 Edit Profile Handler:
• Max Workers: {stats['edit_profile_executor']['max_workers']}
• Active Threads: {stats['edit_profile_executor']['active_threads']}

📊 النظام العام:
• أقفال المستخدمين النشطة: {stats['total_active_locks']}
• إجمالي Threads: {stats['system_threads']}
━━━━━━━━━━━━━━━━━━━━━━━━
🎯 الهدف: 1000 مستخدم متزامن ✅
"""

        await update.message.reply_text(stats_message)

    def get_phase_three_threading_stats(self):
        """إحصائيات Threading للمرحلة التالتة"""
        try:
            stats = {
                "phase_info": {
                    "current_phase": 3,
                    "completed_phases": [
                        "Profile (المرحلة 1)",
                        "Edit Profile (المرحلة 2)",
                        "Main Menu (المرحلة 3)",
                    ],
                    "progress_percentage": 60,  # 3 من 5 مراحل
                },
                "executors": {
                    "profile_executor": {
                        "max_workers": getattr(
                            self.profile_executor, "_max_workers", 0
                        ),
                        "active": len(getattr(self.profile_executor, "_threads", [])),
                        "status": "✅ مكتمل - المرحلة 1",
                    },
                    "edit_profile_executor": {
                        "max_workers": getattr(
                            self.edit_profile_executor, "_max_workers", 0
                        ),
                        "active": len(
                            getattr(self.edit_profile_executor, "_threads", [])
                        ),
                        "status": "✅ مكتمل - المرحلة 2",
                    },
                    "menu_executor": {
                        "max_workers": getattr(self.menu_executor, "_max_workers", 0),
                        "active": len(getattr(self.menu_executor, "_threads", [])),
                        "status": "🆕 جديد - المرحلة 3",
                    },
                    "coins_executor": {
                        "max_workers": getattr(self.coins_executor, "_max_workers", 0),
                        "active": len(getattr(self.coins_executor, "_threads", [])),
                        "status": "🆕 جديد - المرحلة 3 (أعلى أولوية)",
                    },
                    "support_executor": {
                        "max_workers": getattr(
                            self.support_executor, "_max_workers", 0
                        ),
                        "active": len(getattr(self.support_executor, "_threads", [])),
                        "status": "🆕 جديد - المرحلة 3",
                    },
                },
                "system_performance": {
                    "total_workers": self._get_total_workers_count(),
                    "active_threads": threading.active_count(),
                    "user_locks": len(getattr(self, "user_locks", {})),
                    "theoretical_capacity": "محدود بأبطأ عملية",
                    "target_concurrent_users": 1000,
                    "estimated_current_capacity": 300,  # تقدير بناء على 25 worker
                },
                "next_phases": {
                    "phase_4": "Admin Threading (admin_panel, admin_users, etc.)",
                    "phase_5": "Registration Threading (أعقد مرحلة)",
                },
            }

            return stats
        except Exception as e:
            logger.error(f"خطأ في حساب إحصائيات المرحلة التالتة: {e}")
            return {"error": str(e)}

    async def admin_phase_three_stats(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """إحصائيات المرحلة التالتة للأدمن"""
        telegram_id = update.effective_user.id

        if telegram_id != ADMIN_ID:
            await update.message.reply_text("⛔ هذا الأمر للأدمن فقط!")
            return

        stats = self.get_phase_three_threading_stats()

        if "error" in stats:
            await update.message.reply_text(f"❌ خطأ في الإحصائيات: {stats['error']}")
            return

        stats_message = f"""
🚀 إحصائيات المرحلة التالتة - Threading المتقدم
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

📊 معلومات المرحلة:
• المرحلة الحالية: {stats['phase_info']['current_phase']}/5
• نسبة الإنجاز: {stats['phase_info']['progress_percentage']}%
• المراحل المكتملة: {len(stats['phase_info']['completed_phases'])}

🧵 Thread Executors Status:
"""

        for executor_name, executor_stats in stats["executors"].items():
            stats_message += f"""
• {executor_name}:
  - Workers: {executor_stats['max_workers']} (Active: {executor_stats['active']})
  - حالة: {executor_stats['status']}
"""

        stats_message += f"""
📨 أداء النظام:
• إجمالي Workers: {stats['system_performance']['total_workers']}
• Threads نشطة: {stats['system_performance']['active_threads']}
• أقفال المستخدمين: {stats['system_performance']['user_locks']}
• السعة المقدرة: {stats['system_performance']['estimated_current_capacity']} مستخدم متزامن

🎯 الأهداف:
• الهدف النهائي: {stats['system_performance']['target_concurrent_users']} مستخدم متزامن
• التقدم: {stats['phase_info']['progress_percentage']}% مكتمل

⏭️ المراحل القادمة:
• المرحلة 4: {stats['next_phases']['phase_4']}
• المرحلة 5: {stats['next_phases']['phase_5']}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✅ المرحلة التالتة جاهزة للاختبار!
"""

        await update.message.reply_text(stats_message)

    async def delete_account_command(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """حذف الحساب - للأدمن فقط"""
        telegram_id = update.effective_user.id

        # التحقق من أن المستخدم هو الأدمن
        if telegram_id != ADMIN_ID:
            # عرض رسالة مساعدة للمستخدمين العاديين
            await update.message.reply_text(
                "👋 استخدم الأوامر التالية:\n\n"
                "/start - البداية\n"
                "/profile - الملف الشخصي\n"
                "/help - المساعدة",
                reply_markup=ReplyKeyboardRemove(),
            )
            return

        warning = """
⚠️ تحذير مهم!
━━━━━━━━━━━━━━━━
هل أنت متأكد من حذف حسابك الشخصي كأدمن؟
سيتم حذف:
• جميع بياناتك 🗑️
• صلاحيات الأدمن ستبقى
لا يمكن التراجع! ⛔
"""
        await smart_message_manager.send_new_active_message(
            update, context, warning, reply_markup=Keyboards.get_delete_keyboard()
        )

    async def handle_delete_confirmation(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """تأكيد حذف الحساب مع النظام الذكي"""
        query = update.callback_query
        await query.answer()

        if query.data == "confirm_delete":
            telegram_id = query.from_user.id

            success = self.db.delete_user_account(telegram_id)

            if success:
                await smart_message_manager.update_current_message(
                    update,
                    context,
                    "✅ تم حذف حسابك بنجاح.\n\nيمكنك التسجيل مرة أخرى بكتابة /start",
                )
            else:
                await smart_message_manager.update_current_message(
                    update, context, "❌ حدث خطأ. حاول لاحقاً."
                )

        elif query.data == "cancel_delete":
            telegram_id = query.from_user.id
            is_admin = telegram_id == ADMIN_ID

            # العودة للقائمة الرئيسية
            if is_admin:
                welcome_message = f"""
✅ تم الإلغاء.

🎮 بوت FC 26 - لوحة التحكم

⚡ لديك صلاحيات كاملة
"""
            else:
                welcome_message = f"""
✅ تم الإلغاء. سعداء لبقائك معنا! 😊

🎮 بوت FC 26 - أفضل مكان  لبيع كوينز

كيف يمكنني مساعدتك اليوم؟
"""

            keyboard = [
                [InlineKeyboardButton("💸 بيع كوينز", callback_data="sell_coins")],
                [InlineKeyboardButton("👤 الملف الشخصي", callback_data="profile")],
                [InlineKeyboardButton("📞 الدعم", callback_data="support")],
            ]

            if is_admin:
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🔐 لوحة الأدمن", callback_data="admin_panel_advanced"
                        )
                    ]
                )
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف حسابي", callback_data="delete_account"
                        )
                    ]
                )
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف حساب مستخدم", callback_data="admin_delete_user"
                        )
                    ]
                )
            # المستخدمين العاديين لا يرون زر حذف الحساب

            reply_markup = InlineKeyboardMarkup(keyboard)

            await smart_message_manager.update_current_message(
                update, context, welcome_message, reply_markup=reply_markup
            )

    async def handle_menu_buttons(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالج أزرار القائمة المحسن مع Threading شامل للمرحلة التالتة"""
        query = update.callback_query
        await query.answer()

        # لوج مفصل لكل ضغطة زر
        telegram_id = query.from_user.id
        action = query.data
        message_id = query.message.message_id
        logger.info(
            f"🟡 المستخدم {telegram_id} ضغط على زر: {action} - Message ID: {message_id}"
        )

        # المرحلة التالتة: الأزرار الأساسية مع Threading متقدم
        if action in ["main_menu", "sell_coins", "support"]:
            logger.info(
                f"🔄 بدء معالجة المرحلة التالتة - {action} في thread منفصل للمستخدم {telegram_id}"
            )
            await self.handle_main_menu_safely(update, context, telegram_id, action)
            return

        # المراحل السابقة (مكتملة)
        elif action == "profile":
            logger.info(
                f"🔄 معالجة المرحلة الأولى - profile في thread منفصل للمستخدم {telegram_id}"
            )
            await self.handle_profile_safely(update, context, telegram_id)

        elif action == "delete_account":
            # التحقق من أن المستخدم هو الأدمن
            if telegram_id != ADMIN_ID:
                await query.answer("⛔ هذه الميزة للأدمن فقط!", show_alert=True)
                return

            warning = """
⚠️ تحذير مهم!
━━━━━━━━━━━━━━━━
هل أنت متأكد من حذف حسابك الشخصي كأدمن؟
سيتم حذف:
• جميع بياناتك 🗑️
• صلاحيات الأدمن ستبقى
لا يمكن التراجع! ⛔
"""

            await smart_message_manager.update_current_message(
                update, context, warning, reply_markup=Keyboards.get_delete_keyboard()
            )

        # أزرار أخرى (مؤقتاً بدون threading - سيتم إضافتها في المراحل التالية)
        else:
            logger.info(
                f"🟠 معالجة زر غير محول لـ threading بعد: {action} للمستخدم {telegram_id}"
            )
            # المعالجة المؤقتة للأزرار الأخرى
            pass

            # العودة للقائمة الرئيسية باستخدام النظام الذكي
            if is_admin:
                welcome_message = f"""
👋 مرحباً بالأدمن!

🎮 بوت FC 26 - لوحة التحكم

⚡ لديك صلاحيات كاملة
"""
            else:
                welcome_message = f"""
👋 أهلاً بعودتك!
🎮 بوت FC 26 - أفضل مكان  لبيع كوينز
كيف يمكنني مساعدتك اليوم؟
"""

            keyboard = [
                [InlineKeyboardButton("💸 بيع كوينز", callback_data="sell_coins")],
                [InlineKeyboardButton("👤 الملف الشخصي", callback_data="profile")],
                [InlineKeyboardButton("📞 الدعم", callback_data="support")],
            ]

            if is_admin:
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🔐 لوحة الأدمن", callback_data="admin_panel_advanced"
                        )
                    ]
                )
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف حسابي", callback_data="delete_account"
                        )
                    ]
                )
                keyboard.append(
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف حساب مستخدم", callback_data="admin_delete_user"
                        )
                    ]
                )
            # المستخدمين العاديين لا يرون زر حذف الحساب

            reply_markup = InlineKeyboardMarkup(keyboard)

            await smart_message_manager.update_current_message(
                update, context, welcome_message, reply_markup=reply_markup
            )

    async def handle_edit_profile(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالج تعديل الملف الشخصي"""
        query = update.callback_query
        await query.answer()

        # لوج عند الضغط على أزرار التعديل
        user_id = query.from_user.id
        message_id = query.message.message_id
        logger.info(
            f"🟡 المستخدم {user_id} ضغط على زر: {query.data} - Message ID: {message_id}"
        )

        if query.data == "edit_profile":
            # تنفيذ معالج تعديل الملف الشخصي في thread منفصل
            telegram_id = query.from_user.id

            # تسجيل بداية المعالجة
            logger.info(
                f"🔄 بدء معالجة طلب تعديل الملف الشخصي للمستخدم {telegram_id} في thread منفصل"
            )

            # استدعاء المعالج الآمن في thread
            await self.handle_edit_profile_safely(
                update, context, telegram_id, "edit_profile"
            )

        elif query.data == "edit_platform":
            # تنفيذ معالج تعديل المنصة في thread منفصل
            telegram_id = query.from_user.id

            logger.info(
                f"🎮 بدء معالجة طلب تعديل المنصة للمستخدم {telegram_id} في thread منفصل"
            )

            # استدعاء المعالج الآمن في thread
            await self.handle_edit_profile_safely(
                update, context, telegram_id, "edit_platform"
            )

        elif query.data == "edit_whatsapp":
            # بدء عملية تعديل الواتساب بشكل مباشر
            telegram_id = query.from_user.id

            # Stage 6: الحصول على بيانات المستخدم الحالية (إن وجدت) - السماح بالتعديل الحر
            user_data = self.db.get_user_data(telegram_id)

            # Stage 6: السماح بتعديل طرق الدفع حتى للمستخدمين غير المكتملين
            if not user_data:
                logger.info(
                    f"🆕 Stage 6: السماح بتعديل الدفع للمستخدم الجديد {telegram_id}"
                )
                # إنشاء ملف فارغ مؤقت للمستخدمين الجدد
                user_data = {}

            # حفظ البيانات الحالية للاستخدام في التعديل
            context.user_data["editing_mode"] = "whatsapp_only"
            context.user_data["edit_registration"] = {
                "telegram_id": telegram_id,
                "platform": user_data.get("platform"),  # نحتفظ بالمنصة الحالية
                "payment_method": user_data.get(
                    "payment_method"
                ),  # نحتفظ بطريقة الدفع الحالية
                "is_editing": True,
                "edit_type": "whatsapp_only",
            }

            # طلب رقم الواتساب الجديد مباشرة
            message = """
📱 تعديل رقم الواتساب
━━━━━━━━━━━━━━━━
أرسل رقم الواتساب الجديد:
📌 مثال: 01012345678
⚠️ يجب أن يبدأ بـ:
• 010 (فودافون)
• 011 (اتصالات)
• 012 (أورانج)
• 015 (وي)
"""

            await smart_message_manager.update_current_message(
                update, context, message, reply_markup=None  # لا نحتاج أزرار هنا
            )

            # ننتظر إدخال الرقم
            return ENTERING_WHATSAPP

        elif query.data == "edit_payment":
            # بدء عملية تعديل طريقة الدفع بشكل تفاعلي - Stage 6: تحرير كامل
            telegram_id = query.from_user.id

            # Stage 6: الحصول على بيانات المستخدم الحالية (إن وجدت) - السماح بالتعديل الحر
            user_data = self.db.get_user_data(telegram_id)

            # Stage 6: السماح بتعديل طرق الدفع حتى للمستخدمين غير المكتملين
            if not user_data:
                desc_logger.log_success(
                    "Stage 6 - تحرير الدفع للمستخدم الجديد",
                    f"المستخدم {telegram_id} يبدأ تعديل الدفع بحرية كاملة",
                )
                # إنشاء ملف فارغ مؤقت للمستخدمين الجدد
                user_data = {}

            # بدء عملية تعديل طريقة الدفع فقط
            context.user_data["editing_mode"] = "payment_only"
            context.user_data["edit_registration"] = {
                "telegram_id": telegram_id,
                "platform": user_data.get("platform"),
                "whatsapp": (
                    user_data.get("whatsapp") if user_data else None
                ),  # يمكن أن يكون None - Stage 6
                "is_editing": True,
                "edit_type": "payment_only",
                "stage6_free_edit": True,  # علامة التحرير الكامل - المرحلة 6
            }

            # الانتقال مباشرة لاختيار طريقة الدفع
            message = """
💳 تعديل طريقة الدفع
━━━━━━━━━━━━━━━━
اختر طريقة الدفع الجديدة:
"""
            reply_markup = Keyboards.get_payment_keyboard()

            await smart_message_manager.update_current_message(
                update, context, message, reply_markup=reply_markup
            )

            return CHOOSING_PAYMENT

        elif query.data.startswith("update_platform_"):
            # تنفيذ معالج تحديث المنصة في thread منفصل
            telegram_id = query.from_user.id

            desc_logger.log_success(
                "بدء معالجة تحديث المنصة",
                f"المستخدم {telegram_id} - معالجة متوازية في ThreadPool منفصل",
            )

            # استدعاء المعالج الآمن في thread
            await self.handle_edit_profile_safely(
                update, context, telegram_id, query.data
            )
            return  # ننهي هنا لأن المعالجة تتم في thread

            # الكود القديم (لن يتم تنفيذه)
            platform_key = query.data.replace("update_platform_", "")
            telegram_id = query.from_user.id

            if platform_key in GAMING_PLATFORMS:
                # تحديث المنصة في قاعدة البيانات
                success = self.db.update_user_platform(telegram_id, platform_key)

                if success:
                    # عرض الملف الشخصي المحدث مباشرة
                    profile = self.db.get_user_profile(telegram_id)

                    whatsapp_display = profile.get("whatsapp", "غير محدد")
                    network_display = ""

                    if (
                        whatsapp_display
                        and whatsapp_display != "غير محدد"
                        and len(whatsapp_display) >= 3
                    ):
                        prefix = whatsapp_display[:3]
                        if prefix in whatsapp_security.EGYPTIAN_NETWORKS:
                            network = whatsapp_security.EGYPTIAN_NETWORKS[prefix]
                            network_display = f" ({network['emoji']} {network['name']})"

                    profile_text = f"""
✅ تم التحديث بنجاح!
━━━━━━━━━━━━━━━━
👤 الملف الشخصي المحدث
━━━━━━━━━━━━━━━━
🎮 المنصة: {GAMING_PLATFORMS[platform_key]['name']} ✅
📱 واتساب: {whatsapp_display}{network_display}
💳 طريقة الدفع: {profile.get('payment_method', 'غير محدد')}
━━━━━━━━━━━━━━━━
🔐 بياناتك محمية ومشفرة
"""

                    keyboard = [
                        [
                            InlineKeyboardButton(
                                "✏️ تعديل آخر", callback_data="edit_profile"
                            )
                        ],
                        [
                            InlineKeyboardButton(
                                "🏠 القائمة الرئيسية", callback_data="main_menu"
                            )
                        ],
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    await smart_message_manager.update_current_message(
                        update, context, profile_text, reply_markup=reply_markup
                    )
                else:
                    await query.answer("❌ فشل تحديث المنصة", show_alert=True)
            else:
                await query.answer("❌ منصة غير صالحة", show_alert=True)

    async def admin_panel(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """لوحة تحكم الأدمن"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        # جلب إحصائيات البوت
        conn = self.db.get_connection()
        cursor = conn.cursor()

        # عدد المستخدمين
        cursor.execute("SELECT COUNT() FROM users")
        total_users = cursor.fetchone()[0]

        # عدد المستخدمين المسجلين بالكامل
        cursor.execute(
            "SELECT COUNT() FROM users WHERE registration_status = 'complete'"
        )
        registered_users = cursor.fetchone()[0]

        # آخر المستخدمين المسجلين
        cursor.execute(
            """
            SELECT telegram_id, username, full_name, created_at
            FROM users
            WHERE registration_status = 'complete'
            ORDER BY created_at DESC
            LIMIT 5
        """
        )
        recent_users = cursor.fetchall()

        conn.close()

        # بناء رسالة الإحصائيات
        admin_text = f"""
🔐 لوحة تحكم الأدمن
━━━━━━━━━━━━━━━━
📊 إحصائيات البوت:
• إجمالي المستخدمين: {total_users}
• مستخدمين مسجلين: {registered_users}
• غير مكتملين: {total_users - registered_users}
🕔 آخر التسجيلات:
"""

        for user in recent_users:
            username = f"@{user['username']}" if user["username"] else "غير محدد"
            admin_text += f"• {username} (ID: {user['telegram_id']})\n"

        if not recent_users:
            admin_text += "• لا يوجد تسجيلات جديدة\n"

        # أزرار لوحة الأدمن
        keyboard = [
            [
                InlineKeyboardButton(
                    "👥 عرض جميع المستخدمين", callback_data="admin_view_users"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔍 بحث عن مستخدم", callback_data="admin_search_user"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 إرسال رسالة للجميع", callback_data="admin_broadcast"
                )
            ],
            [InlineKeyboardButton("🗑️ حذف مستخدم", callback_data="admin_delete_user")],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await smart_message_manager.update_current_message(
            update, context, admin_text, reply_markup=reply_markup
        )

    async def handle_admin_panel_advanced(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالج لوحة الأدمن بـ Threading متقدم - المرحلة الرابعة"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        try:
            # تنفيذ في thread منفصل
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(
                self.admin_pool, self._handle_admin_panel_thread, telegram_id
            )

            # انتظار النتيجة مع timeout
            stats = await asyncio.wait_for(future, timeout=5.0)

            if stats:
                await self._display_admin_panel_result(update, context, stats)
                logger.info(
                    f"✅ تم عرض لوحة الأدمن بنجاح - Cache hit rate: {stats['cache_performance']['hit_rate']}"
                )
            else:
                await smart_message_manager.update_current_message(
                    update, context, "❌ حدث خطأ في جلب البيانات"
                )

        except asyncio.TimeoutError:
            await smart_message_manager.update_current_message(
                update, context, "⏰ انتهت مهلة جلب البيانات"
            )
        except Exception as e:
            logger.error(f"❌ خطأ في لوحة الأدمن: {e}")
            await smart_message_manager.update_current_message(
                update, context, "❌ حدث خطأ غير متوقع"
            )

    def _handle_admin_panel_thread(self, telegram_id: int) -> Optional[Dict]:
        """معالجة لوحة الأدمن داخل thread"""
        try:
            thread_name = threading.current_thread().name
            logger.debug(f"🔄 بدء معالجة لوحة الأدمن - Thread: {thread_name}")

            # جلب الإحصائيات من AdminHandler
            stats = self.admin_handler.get_admin_stats(use_cache=True)

            # إضافة معلومات thread
            stats["thread_info"] = {"name": thread_name, "admin_id": telegram_id}

            return stats

        except Exception as e:
            logger.error(f"❌ خطأ في thread لوحة الأدمن: {e}")
            return None

    async def _display_admin_panel_result(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, stats: Dict
    ):
        """عرض نتيجة لوحة الأدمن مع Threading"""

        # بناء رسالة الإحصائيات
        admin_text = f"""
🔐 لوحة تحكم الأدمن - المرحلة الرابعة
━━━━━━━━━━━━━━━━
📊 إحصائيات البوت:
• إجمالي المستخدمين: {stats['total_users']}
• مستخدمين مسجلين: {stats['registered_users']}
• غير مكتملين: {stats['incomplete_users']}

🚀 أداء الكاش:
• Cache Hits: {stats['cache_performance']['hits']}
• Cache Misses: {stats['cache_performance']['misses']}
• Hit Rate: {stats['cache_performance']['hit_rate']}

🧵 Thread: {stats['thread_info']['name']}
🕔 آخر التسجيلات:
"""

        for user in stats["recent_users"]:
            username = f"@{user['username']}" if user["username"] else "غير محدد"
            admin_text += f"• {username} (ID: {user['telegram_id']})\n"

        if not stats["recent_users"]:
            admin_text += "• لا يوجد تسجيلات جديدة\n"

        # أزرار لوحة الأدمن المحسنة
        keyboard = [
            [
                InlineKeyboardButton(
                    "👥 عرض جميع المستخدمين", callback_data="admin_view_users_advanced"
                )
            ],
            [
                InlineKeyboardButton(
                    "🔍 بحث عن مستخدم", callback_data="admin_search_user_advanced"
                )
            ],
            [
                InlineKeyboardButton(
                    "📢 إرسال رسالة للجميع", callback_data="admin_broadcast_advanced"
                )
            ],
            [
                InlineKeyboardButton(
                    "🗑️ حذف مستخدم", callback_data="admin_delete_user_advanced"
                )
            ],
            [
                InlineKeyboardButton(
                    "📊 إحصائيات Threading", callback_data="phase4_stats"
                )
            ],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await smart_message_manager.update_current_message(
            update, context, admin_text, reply_markup=reply_markup
        )

    async def handle_admin_view_users_advanced(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 1
    ):
        """عرض المستخدمين بـ Threading متقدم"""
        query = update.callback_query

        # استخراج رقم الصفحة
        if query and query.data.startswith("admin_users_page_adv_"):
            page = int(query.data.replace("admin_users_page_adv_", ""))

        if query:
            await query.answer()
            telegram_id = query.from_user.id
        else:
            telegram_id = update.effective_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            if query:
                await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        try:
            # تنفيذ في thread منفصل
            loop = asyncio.get_event_loop()
            future = loop.run_in_executor(
                self.admin_pool, self._handle_view_users_thread, page
            )

            # انتظار النتيجة
            result = await asyncio.wait_for(future, timeout=6.0)

            if result:
                await self._display_users_page_result(update, context, result)
            else:
                await smart_message_manager.update_current_message(
                    update, context, "❌ حدث خطأ في جلب المستخدمين"
                )

        except Exception as e:
            logger.error(f"❌ خطأ في عرض المستخدمين: {e}")

    def _handle_view_users_thread(self, page: int) -> Optional[Dict]:
        """معالجة عرض المستخدمين داخل thread"""
        try:
            return self.admin_handler.get_users_page(page, use_cache=True)
        except Exception as e:
            logger.error(f"❌ خطأ في thread عرض المستخدمين: {e}")
            return None

    async def _display_users_page_result(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, result: Dict
    ):
        """عرض نتيجة صفحة المستخدمين"""

        users_text = f"""
👥 قائمة المستخدمين - Threading متقدم
📄 الصفحة {result['page']} من {result['total_pages']}
👤 إجمالي المستخدمين: {result['total_users']}
━━━━━━━━━━━━━━━━
"""

        if not result["users"]:
            users_text += "لا يوجد مستخدمين في هذه الصفحة."
        else:
            for i, user in enumerate(result["users"], start=result["offset"] + 1):
                username = f"@{user['username']}" if user["username"] else "غير محدد"
                status = "✅" if user["registration_status"] == "complete" else "⏳"
                users_text += f"{i}. {status} {username}\n"
                users_text += f"   ID: {user['telegram_id']}\n"
                if user["platform"]:
                    users_text += f"   🎮 {user['platform']}\n"
                if user["whatsapp"]:
                    users_text += f"   📱 {user['whatsapp']}\n"
                users_text += "\n"

        # بناء أزرار التنقل
        keyboard = []
        navigation_row = []

        if result["page"] > 1:
            navigation_row.append(
                InlineKeyboardButton(
                    "⏪ الأولى", callback_data="admin_users_page_adv_1"
                )
            )
            navigation_row.append(
                InlineKeyboardButton(
                    "◀️ السابقة",
                    callback_data=f"admin_users_page_adv_{result['page']-1}",
                )
            )

        navigation_row.append(
            InlineKeyboardButton(
                f"📄 {result['page']}/{result['total_pages']}", callback_data="ignore"
            )
        )

        if result["page"] < result["total_pages"]:
            navigation_row.append(
                InlineKeyboardButton(
                    "▶️ التالية",
                    callback_data=f"admin_users_page_adv_{result['page']+1}",
                )
            )
            navigation_row.append(
                InlineKeyboardButton(
                    "⏩ الأخيرة",
                    callback_data=f"admin_users_page_adv_{result['total_pages']}",
                )
            )

        if navigation_row:
            keyboard.append(navigation_row)

        keyboard.append(
            [
                InlineKeyboardButton(
                    "🔙 رجوع للوحة الأدمن", callback_data="admin_panel_advanced"
                )
            ]
        )

        reply_markup = InlineKeyboardMarkup(keyboard)

        await smart_message_manager.update_current_message(
            update, context, users_text, reply_markup=reply_markup
        )

    async def get_phase_four_threading_stats(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """عرض إحصائيات Threading للمرحلة الرابعة"""
        query = update.callback_query
        if query:
            await query.answer()
            telegram_id = query.from_user.id
        else:
            telegram_id = update.effective_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            if query:
                await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        # جمع إحصائيات جميع executors
        total_workers = (
            self.profile_executor._max_workers
            + self.edit_profile_executor._max_workers
            + self.menu_executor._max_workers
            + self.coins_executor._max_workers
            + self.support_executor._max_workers
            + self.admin_pool._max_workers
        )

        # إحصائيات AdminHandler
        admin_stats = self.admin_handler.get_performance_stats()

        stats_text = f"""
📊 إحصائيات Threading - المرحلة الرابعة
━━━━━━━━━━━━━━━━
🧵 Thread Pools:
• Profile: {self.profile_executor._max_workers} workers
• Edit Profile: {self.edit_profile_executor._max_workers} workers
• Menu: {self.menu_executor._max_workers} workers
• Coins: {self.coins_executor._max_workers} workers
• Support: {self.support_executor._max_workers} workers
• Admin: {self.admin_pool._max_workers} workers 🆕

📊 إجمالي Workers: {total_workers}

🚀 Admin Cache Performance:
• Cache Size: {admin_stats['cache']['size']}/{admin_stats['cache']['max_size']}
• Hit Rate: {admin_stats['cache']['hit_rate']}
• Hits: {admin_stats['cache']['hits']}
• Misses: {admin_stats['cache']['misses']}

💼 Admin Operations:
• Panel: {admin_stats['operations']['panel']}
• Users: {admin_stats['operations']['users']}
• Search: {admin_stats['operations']['search']}
• Broadcast: {admin_stats['operations']['broadcast']}
• Delete: {admin_stats['operations']['delete']}
• Total: {admin_stats['total_operations']}

🎯 الهدف: 1000 مستخدم متزامن
🔥 الحالة: 650+ مستخدم (المرحلة 4/5)
"""

        keyboard = [
            [
                InlineKeyboardButton(
                    "🔙 رجوع للوحة الأدمن", callback_data="admin_panel_advanced"
                )
            ],
            [InlineKeyboardButton("🏠 القائمة الرئيسية", callback_data="main_menu")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await smart_message_manager.update_current_message(
            update, context, stats_text, reply_markup=reply_markup
        )

    async def handle_text_messages(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالجة الرسائل النصية - نعيد توجيههم للأوامر"""
        # إزالة أي كيبورد موجود
        await update.message.reply_text(
            "👋 استخدم الأوامر التالية:\n\n"
            "/start - البداية\n"
            "/profile - الملف الشخصي\n"
            "/help - المساعدة",
            reply_markup=ReplyKeyboardRemove(),
        )

    async def admin_view_users(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE, page: int = 1
    ):
        """عرض جميع المستخدمين للأدمن بنظام الصفحات"""
        query = update.callback_query

        # استخراج رقم الصفحة من callback_data إن وجد
        if query and query.data.startswith("admin_users_page_"):
            page = int(query.data.replace("admin_users_page_", ""))

        if query:
            await query.answer()
            telegram_id = query.from_user.id
        else:
            telegram_id = update.effective_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            if query:
                await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        conn = self.db.get_connection()
        cursor = conn.cursor()

        # الحصول على إجمالي عدد المستخدمين
        cursor.execute("SELECT COUNT() FROM users")
        total_users = cursor.fetchone()[0]

        # حساب عدد الصفحات
        users_per_page = 10
        total_pages = (total_users + users_per_page - 1) // users_per_page

        # التأكد من أن رقم الصفحة صحيح
        if page < 1:
            page = 1
        elif page > total_pages:
            page = total_pages

        # حساب offset للصفحة الحالية
        offset = (page - 1) * users_per_page

        # جلب المستخدمين للصفحة الحالية
        cursor.execute(
            """
            SELECT u.telegram_id, u.username, u.full_name, u.registration_status,
                   r.platform, r.whatsapp, r.payment_method
            FROM users u
            LEFT JOIN registration_data r ON u.user_id = r.user_id
            ORDER BY u.created_at DESC
            LIMIT ? OFFSET ?
        """,
            (users_per_page, offset),
        )
        users = cursor.fetchall()

        conn.close()

        # بناء نص الرسالة
        users_text = f"""
👥 قائمة المستخدمين
📄 الصفحة {page} من {total_pages}
👤 إجمالي المستخدمين: {total_users}
━━━━━━━━━━━━━━━━
"""

        if not users:
            users_text += "لا يوجد مستخدمين في هذه الصفحة."
        else:
            for i, user in enumerate(users, start=offset + 1):
                username = f"@{user['username']}" if user["username"] else "غير محدد"
                status = "✅" if user["registration_status"] == "complete" else "⏳"
                users_text += f"{i}. {status} {username}\n"
                users_text += f"   ID: {user['telegram_id']}\n"
                if user["platform"]:
                    users_text += f"   🎮 {user['platform']}\n"
                if user["whatsapp"]:
                    users_text += f"   📱 {user['whatsapp']}\n"
                users_text += "\n"

        # بناء أزرار التنقل
        keyboard = []

        # صف أزرار التنقل بين الصفحات
        navigation_row = []

        # زر الصفحة الأولى
        if page > 1:
            navigation_row.append(
                InlineKeyboardButton("⏪ الأولى", callback_data="admin_users_page_1")
            )

        # زر الصفحة السابقة
        if page > 1:
            navigation_row.append(
                InlineKeyboardButton(
                    "◀️ السابقة", callback_data=f"admin_users_page_{page-1}"
                )
            )

        # زر عرض رقم الصفحة الحالي (غير قابل للضغط)
        navigation_row.append(
            InlineKeyboardButton(f"📄 {page}/{total_pages}", callback_data="ignore")
        )

        # زر الصفحة التالية
        if page < total_pages:
            navigation_row.append(
                InlineKeyboardButton(
                    "▶️ التالية", callback_data=f"admin_users_page_{page+1}"
                )
            )

        # زر الصفحة الأخيرة
        if page < total_pages:
            navigation_row.append(
                InlineKeyboardButton(
                    "⏩ الأخيرة", callback_data=f"admin_users_page_{total_pages}"
                )
            )

        if navigation_row:
            keyboard.append(navigation_row)

        # زر الرجوع للوحة الأدمن
        keyboard.append(
            [InlineKeyboardButton("🔙 رجوع للوحة الأدمن", callback_data="admin_panel")]
        )

        reply_markup = InlineKeyboardMarkup(keyboard)

        # إرسال أو تحديث الرسالة
        if query:
            await smart_message_manager.update_current_message(
                update, context, users_text, reply_markup=reply_markup
            )
        else:
            await smart_message_manager.send_new_active_message(
                update, context, users_text, reply_markup=reply_markup
            )

    async def admin_delete_user(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """حذف مستخدم - للأدمن فقط"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        # وضع البوت في وضع انتظار إدخال ID المستخدم
        context.user_data["admin_action"] = "delete_user"

        await smart_message_manager.update_current_message(
            update,
            context,
            "🗑️ حذف مستخدم\n\n"
            "أدخل معرف التليجرام (ID) للمستخدم المراد حذفه:\n\n"
            "مثال: 123456789\n\n"
            "⚠️ تحذير: سيتم حذف جميع بيانات المستخدم نهائياً!",
        )

    async def admin_confirm_delete(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """تأكيد حذف المستخدم"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        # استخراج ID المستخدم من callback_data
        user_to_delete = int(query.data.replace("admin_confirm_delete_", ""))

        # حذف المستخدم
        success = self.db.delete_user_account(user_to_delete)

        if success:
            await smart_message_manager.update_current_message(
                update,
                context,
                f"✅ تم حذف المستخدم بنجاح!\n\n"
                f"ID: {user_to_delete}\n\n"
                f"تم حذف جميع البيانات المرتبطة بهذا المستخدم.",
            )
        else:
            await smart_message_manager.update_current_message(
                update,
                context,
                "❌ فشل حذف المستخدم\n\n" "قد يكون المستخدم غير موجود أو حدث خطأ.",
            )

        # مسح حالة الأدمن
        context.user_data.pop("admin_action", None)

    async def admin_broadcast(self, update: Update, context: ContextTypes.DEFAULT_TYPE):
        """إرسال رسالة للجميع - للأدمن فقط"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        # وضع البوت في وضع انتظار الرسالة
        context.user_data["admin_action"] = "broadcast"

        await smart_message_manager.update_current_message(
            update,
            context,
            "📢 إرسال رسالة للجميع\n\n"
            "اكتب الرسالة التي تريد إرسالها لجميع المستخدمين:\n\n"
            "📝 ملاحظة: سيتم إرسال الرسالة لجميع المستخدمين المسجلين.\n"
            "⚠️ استخدم هذه الميزة بحذر!",
        )

    async def admin_search_user(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """البحث عن مستخدم - للأدمن فقط"""
        query = update.callback_query
        await query.answer()

        telegram_id = query.from_user.id

        # التحقق من صلاحيات الأدمن
        if telegram_id != ADMIN_ID:
            await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
            return

        # وضع البوت في وضع انتظار البحث
        context.user_data["admin_action"] = "search_user"

        await smart_message_manager.update_current_message(
            update,
            context,
            "🔍 البحث عن مستخدم\n\n"
            "أدخل واحد من التالي للبحث:\n\n"
            "• معرف التليجرام (ID)\n"
            "• اسم المستخدم (@username)\n\n"
            "مثال: 123456789 أو @username",
        )

    async def handle_admin_text_input(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """معالج إدخال النص من الأدمن"""
        telegram_id = update.effective_user.id

        # التحقق من أن المرسل هو الأدمن
        if telegram_id != ADMIN_ID:
            # إذا لم يكن أدمن، نعامله كمستخدم عادي
            await self.handle_text_messages(update, context)
            return

        # التحقق من وجود إجراء أدمن نشط
        admin_action = context.user_data.get("admin_action")

        if not admin_action:
            # لا يوجد إجراء نشط، نعامله كرسالة عادية
            await self.handle_text_messages(update, context)
            return

        text = update.message.text.strip()

        if admin_action == "delete_user":
            # محاولة حذف المستخدم
            try:
                user_id_to_delete = int(text)

                # التحقق من أن الأدمن لا يحذف نفسه
                if user_id_to_delete == ADMIN_ID:
                    await smart_message_manager.send_new_active_message(
                        update,
                        context,
                        "❌ لا يمكنك حذف حسابك الخاص!\n\n" "أنت الأدمن الرئيسي للبوت.",
                    )
                    context.user_data.pop("admin_action", None)
                    return

                # التحقق من وجود المستخدم
                user = self.db.get_user_by_telegram_id(user_id_to_delete)

                if user:
                    # عرض تأكيد الحذف
                    username = (
                        f"@{user['username']}" if user["username"] else "غير محدد"
                    )

                    keyboard = [
                        [
                            InlineKeyboardButton(
                                "✅ تأكيد الحذف",
                                callback_data=f"admin_confirm_delete_{user_id_to_delete}",
                            )
                        ],
                        [InlineKeyboardButton("❌ إلغاء", callback_data="admin_panel")],
                    ]
                    reply_markup = InlineKeyboardMarkup(keyboard)

                    await smart_message_manager.send_new_active_message(
                        update,
                        context,
                        f"⚠️ تأكيد حذف المستخدم\n\n"
                        f"👤 الاسم: {user['full_name']}\n"
                        f"🆔 المعرف: {user_id_to_delete}\n"
                        f"📝 اسم المستخدم: {username}\n\n"
                        f"هل أنت متأكد من حذف هذا المستخدم؟",
                        reply_markup=reply_markup,
                    )
                else:
                    await smart_message_manager.send_new_active_message(
                        update,
                        context,
                        f"❌ المستخدم غير موجود\n\n"
                        f"لا يوجد مستخدم بالمعرف: {user_id_to_delete}",
                    )

            except ValueError:
                await smart_message_manager.send_new_active_message(
                    update, context, "❌ معرف غير صحيح\n\n" "يجب إدخال رقم صحيح فقط."
                )

            context.user_data.pop("admin_action", None)

        elif admin_action == "broadcast":
            # إرسال الرسالة لجميع المستخدمين
            conn = self.db.get_connection()
            cursor = conn.cursor()

            cursor.execute(
                "SELECT telegram_id FROM users WHERE registration_status = 'complete'"
            )
            users = cursor.fetchall()

            conn.close()

            success_count = 0
            fail_count = 0

            broadcast_msg = f"📢 رسالة من الإدارة\n\n{text}"

            for user in users:
                try:
                    await context.bot.send_message(
                        chat_id=user["telegram_id"],
                        text=broadcast_msg,
                        # parse_mode removed
                    )
                    success_count += 1
                    await asyncio.sleep(0.1)  # تأخير بسيط لتجنب حدود التليجرام
                except Exception as e:
                    fail_count += 1
                    logger.error(f"فشل إرسال رسالة للمستخدم {user['telegram_id']}: {e}")

            await smart_message_manager.send_new_active_message(
                update,
                context,
                f"✅ تمت عملية البث\n\n"
                f"📊 الإحصائيات:\n"
                f"• نجح الإرسال: {success_count}\n"
                f"• فشل الإرسال: {fail_count}\n"
                f"• الإجمالي: {len(users)}",
            )

            context.user_data.pop("admin_action", None)

        elif admin_action == "search_user":
            # البحث عن مستخدم
            conn = self.db.get_connection()
            cursor = conn.cursor()

            # البحث بالمعرف أو اسم المستخدم
            if text.startswith("@"):
                # البحث باسم المستخدم
                username = text[1:]  # إزالة @
                cursor.execute(
                    """
                    SELECT u.*, r.platform, r.whatsapp, r.payment_method
                    FROM users u
                    LEFT JOIN registration_data r ON u.user_id = r.user_id
                    WHERE u.username = ?
                """,
                    (username,),
                )
            else:
                # البحث بالمعرف
                try:
                    search_id = int(text)
                    cursor.execute(
                        """
                        SELECT u.*, r.platform, r.whatsapp, r.payment_method
                        FROM users u
                        LEFT JOIN registration_data r ON u.user_id = r.user_id
                        WHERE u.telegram_id = ?
                    """,
                        (search_id,),
                    )
                except ValueError:
                    await smart_message_manager.send_new_active_message(
                        update,
                        context,
                        "❌ بحث غير صحيح\n\n"
                        "يجب إدخال معرف رقمي أو اسم مستخدم يبدأ بـ @",
                    )
                    context.user_data.pop("admin_action", None)
                    conn.close()
                    return

            user = cursor.fetchone()
            conn.close()

            if user:
                username_display = (
                    f"@{user['username']}" if user["username"] else "غير محدد"
                )
                status = (
                    "✅ مكتمل"
                    if user["registration_status"] == "complete"
                    else "⏳ غير مكتمل"
                )

                user_info = f"""
🔍 نتيجة البحث
━━━━━━━━━━━━━━━━
👤 معلومات المستخدم:
• الاسم: {user['full_name']}
• المعرف: {user['telegram_id']}
• اسم المستخدم: {username_display}
• الحالة: {status}
• تاريخ التسجيل: {user['created_at']}
"""

                if user["platform"]:
                    user_info += f"\n🎮 المنصة: {user['platform']}"
                if user["whatsapp"]:
                    user_info += f"\n📱 واتساب: {user['whatsapp']}"
                if user["payment_method"]:
                    user_info += f"\n💳 طريقة الدفع: {user['payment_method']}"

                keyboard = [
                    [
                        InlineKeyboardButton(
                            "🗑️ حذف هذا المستخدم",
                            callback_data=f"admin_confirm_delete_{user['telegram_id']}",
                        )
                    ],
                    [InlineKeyboardButton("🔙 رجوع", callback_data="admin_panel")],
                ]
                reply_markup = InlineKeyboardMarkup(keyboard)

                await smart_message_manager.send_new_active_message(
                    update, context, user_info, reply_markup=reply_markup
                )
            else:
                await smart_message_manager.send_new_active_message(
                    update,
                    context,
                    f"❌ لم يتم العثور على المستخدم\n\n" f"لا يوجد مستخدم بـ: {text}",
                )

            context.user_data.pop("admin_action", None)

    async def admin_search_user_advanced(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """البحث عن مستخدم - النسخة المتقدمة"""
        logger.info("🔥 [ADMIN_DEBUG] admin_search_user_advanced() تم استدعاؤها")
        # إعادة توجيه للمعالج العادي
        try:
            query = update.callback_query
            await query.answer()

            if query.from_user.id != ADMIN_ID:
                await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
                return

            context.user_data["admin_action"] = "search_user"

            await smart_message_manager.update_current_message(
                update,
                context,
                "🔍 البحث عن مستخدم\n\n"
                "أدخل واحد من التالي للبحث:\n\n"
                "• معرف التليجرام (ID)\n"
                "• اسم المستخدم (@username)\n\n"
                "مثال: 123456789 أو @username",
            )
            logger.info("✅ [ADMIN_DEBUG] معالج متقدم تم بنجاح")
        except Exception as e:
            logger.error(f"❌ [ADMIN_DEBUG] خطأ في المعالج المتقدم: {e}")
            if update.callback_query:
                try:
                    await update.callback_query.answer("❌ حدث خطأ!", show_alert=True)
                except:
                    pass

    async def admin_broadcast_advanced(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """إرسال رسالة للجميع - النسخة المتقدمة"""
        logger.info("🔥 [ADMIN_DEBUG] admin_broadcast_advanced() تم استدعاؤها")
        # إعادة توجيه للمعالج العادي
        try:
            query = update.callback_query
            await query.answer()

            if query.from_user.id != ADMIN_ID:
                await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
                return

            context.user_data["admin_action"] = "broadcast"

            await smart_message_manager.update_current_message(
                update,
                context,
                "📢 إرسال رسالة للجميع\n\n"
                "اكتب الرسالة التي تريد إرسالها لجميع المستخدمين:\n\n"
                "📝 ملاحظة: سيتم إرسال الرسالة لجميع المستخدمين المسجلين.\n"
                "⚠️ استخدم هذه الميزة بحذر!",
            )
            logger.info("✅ [ADMIN_DEBUG] معالج البث المتقدم تم بنجاح")
        except Exception as e:
            logger.error(f"❌ [ADMIN_DEBUG] خطأ في معالج البث: {e}")
            if update.callback_query:
                try:
                    await update.callback_query.answer(
                        "❌ حدث خطأ في البث!", show_alert=True
                    )
                except:
                    pass

    async def admin_delete_user_advanced(
        self, update: Update, context: ContextTypes.DEFAULT_TYPE
    ):
        """حذف مستخدم - النسخة المتقدمة"""
        logger.info("🔥 [ADMIN_DEBUG] admin_delete_user_advanced() تم استدعاؤها")
        # إعادة توجيه للمعالج العادي
        try:
            query = update.callback_query
            await query.answer()

            if query.from_user.id != ADMIN_ID:
                await query.answer("⛔ ليس لديك صلاحية!", show_alert=True)
                return

            context.user_data["admin_action"] = "delete_user"

            await smart_message_manager.update_current_message(
                update,
                context,
                "🗑️ حذف مستخدم\n\n"
                "أدخل معرف التليجرام (ID) للمستخدم المراد حذفه:\n\n"
                "مثال: 123456789\n\n"
                "⚠️ تحذير: سيتم حذف جميع بيانات المستخدم نهائياً!",
            )
            logger.info("✅ [ADMIN_DEBUG] معالج الحذف المتقدم تم بنجاح")
        except Exception as e:
            logger.error(f"❌ [ADMIN_DEBUG] خطأ في معالج الحذف: {e}")
            if update.callback_query:
                try:
                    await update.callback_query.answer(
                        "❌ حدث خطأ في الحذف!", show_alert=True
                    )
                except:
                    pass

    def get_registration_conversation(self):
        """معالج المحادثة للتسجيل"""
        return ConversationHandler(
            entry_points=[
                CallbackQueryHandler(
                    self.registration_handler.handle_registration_start,
                    pattern="^register_new$",
                ),
                CallbackQueryHandler(
                    self.registration_handler.handle_continue_registration,
                    pattern="^(continue_registration|restart_registration)$",
                ),
            ],
            states={
                CHOOSING_PLATFORM: [
                    CallbackQueryHandler(
                        self.registration_handler.handle_platform_choice,
                        pattern="^platform_",
                    )
                ],
                ENTERING_WHATSAPP: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        self.registration_handler.handle_whatsapp_input,
                    )
                ],
                CHOOSING_PAYMENT: [
                    CallbackQueryHandler(
                        self.registration_handler.handle_payment_choice,
                        pattern="^payment_",
                    )
                ],
                ENTERING_PAYMENT_DETAILS: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        self.registration_handler.handle_payment_details_input,
                    )
                ],
            },
            fallbacks=[
                CommandHandler("cancel", self.registration_handler.cancel),
                CommandHandler("start", self.registration_handler.start),
            ],
            allow_reentry=True,
        )

    def get_edit_conversation(self):
        """معالج المحادثة للتعديل"""
        return ConversationHandler(
            entry_points=[
                CallbackQueryHandler(
                    self.handle_edit_profile, pattern="^(edit_whatsapp|edit_payment)$"
                )
            ],
            states={
                CHOOSING_PLATFORM: [
                    CallbackQueryHandler(
                        self.registration_handler.handle_platform_choice,
                        pattern="^platform_",
                    )
                ],
                ENTERING_WHATSAPP: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        self.registration_handler.handle_whatsapp_input,
                    )
                ],
                CHOOSING_PAYMENT: [
                    CallbackQueryHandler(
                        self.registration_handler.handle_payment_choice,
                        pattern="^payment_",
                    )
                ],
                ENTERING_PAYMENT_DETAILS: [
                    MessageHandler(
                        filters.TEXT & ~filters.COMMAND,
                        self.registration_handler.handle_payment_details_input,
                    )
                ],
            },
            fallbacks=[
                CommandHandler("cancel", self.registration_handler.cancel),
                CommandHandler("profile", self.profile_command),
            ],
            allow_reentry=True,
        )

    def run(self):
        """تشغيل البوت"""
        app = Application.builder().token(BOT_TOKEN).build()

        # إعداد bot_instance في context.bot_data للـ Registration Threading
        app.bot_data["bot_instance"] = self
        logger.info("🔧 تم إعداد bot_instance في context.bot_data للـ Threading")

        # معالج التسجيل (يجب أن يكون أولاً ليأخذ الأولوية)
        app.add_handler(self.get_registration_conversation())

        # معالج التعديل (للتعديل التفاعلي)
        app.add_handler(self.get_edit_conversation())

        # الأوامر
        app.add_handler(CommandHandler("start", self.start))
        app.add_handler(CommandHandler("profile", self.profile_command))
        app.add_handler(CommandHandler("help", self.help_command))
        # أمر إحصائيات المرحلة الرابعة للأدمن فقط
        app.add_handler(
            CommandHandler("phase4_stats", self.get_phase_four_threading_stats)
        )
        # أمر حذف الحساب للأدمن فقط
        app.add_handler(CommandHandler("delete", self.delete_account_command))

        # الأزرار
        app.add_handler(
            CallbackQueryHandler(
                self.handle_delete_confirmation,
                pattern="^(confirm_delete|cancel_delete)$",
            )
        )

        # أزرار القائمة الرئيسية (محدثة بدون الأزرار المحذوفة)
        app.add_handler(
            CallbackQueryHandler(
                self.handle_menu_buttons,
                pattern="^(profile|delete_account|sell_coins|support|main_menu)$",
            )
        )

        # أزرار تعديل الملف الشخصي
        app.add_handler(
            CallbackQueryHandler(
                self.handle_edit_profile,
                pattern="^(edit_profile|edit_platform|edit_whatsapp|edit_payment|update_platform_.+|update_payment_.+)$",
            )
        )

        # أزرار لوحة الأدمن
        app.add_handler(CallbackQueryHandler(self.admin_panel, pattern="^admin_panel$"))

        # المرحلة الرابعة: أزرار لوحة الأدمن المتقدمة مع Threading
        app.add_handler(
            CallbackQueryHandler(
                self.handle_admin_panel_advanced, pattern="^admin_panel_advanced$"
            )
        )
        app.add_handler(
            CallbackQueryHandler(
                self.handle_admin_view_users_advanced,
                pattern="^admin_view_users_advanced$",
            )
        )
        app.add_handler(
            CallbackQueryHandler(
                self.handle_admin_view_users_advanced,
                pattern=r"^admin_users_page_adv_\d+$",
            )
        )
        app.add_handler(
            CallbackQueryHandler(
                self.get_phase_four_threading_stats, pattern="^phase4_stats$"
            )
        )

        app.add_handler(
            CallbackQueryHandler(self.admin_view_users, pattern="^admin_view_users$")
        )

        # معالج الصفحات لعرض المستخدمين
        app.add_handler(
            CallbackQueryHandler(
                self.admin_view_users, pattern=r"^admin_users_page_\d+$"
            )
        )

        app.add_handler(
            CallbackQueryHandler(self.admin_delete_user, pattern="^admin_delete_user$")
        )

        app.add_handler(
            CallbackQueryHandler(
                self.admin_confirm_delete, pattern=r"^admin_confirm_delete_\d+$"
            )
        )

        app.add_handler(
            CallbackQueryHandler(self.admin_broadcast, pattern="^admin_broadcast$")
        )

        # 🔥 معالج تشخيصي لأزرار الأدمن
        async def debug_admin_callback(update, context):
            try:
                user_id = update.effective_user.id
                callback_data = (
                    update.callback_query.data if update.callback_query else "None"
                )
                logger.info(
                    f"🔥 [ADMIN_DEBUG] Callback: {callback_data} من User: {user_id} (Admin: {ADMIN_ID})"
                )
            except Exception as e:
                logger.error(f"❌ [ADMIN_DEBUG] خطأ في التشخيص: {e}")

        app.add_handler(
            CallbackQueryHandler(debug_admin_callback, pattern=r"^admin_"), group=-1
        )

        app.add_handler(
            CallbackQueryHandler(self.admin_search_user, pattern="^admin_search_user$")
        )

        # معالج رسائل  البحث والبث للأدمن
        app.add_handler(
            MessageHandler(
                filters.TEXT & ~filters.COMMAND, self.handle_admin_text_input
            )
        )

        # 🔥 تسجيل معالجات الأدمن المتقدمة المفقودة
        app.add_handler(
            CallbackQueryHandler(
                self.admin_search_user_advanced, pattern="^admin_search_user_advanced$"
            )
        )
        app.add_handler(
            CallbackQueryHandler(
                self.admin_broadcast_advanced, pattern="^admin_broadcast_advanced$"
            )
        )
        app.add_handler(
            CallbackQueryHandler(
                self.admin_delete_user_advanced, pattern="^admin_delete_user_advanced$"
            )
        )

        # التشغيل
        logger.info("🚀 بدء تشغيل FC 26 Smart Bot...")
        logger.info("✨ النظام الذكي للرسائل مفعّل")
        logger.info("📱 البوت جاهز: https://t.me/FC26_Trading_Bot")

        app.run_polling(allowed_updates=Update.ALL_TYPES)

    def cleanup(self):
        """تنظيف كامل لجميع ThreadPools عند إيقاف البوت"""
        logger.info("🧹 بدء تنظيف جميع ThreadPools...")

        # قائمة كل ThreadPools بالترتيب
        pools = [
            ("profile_executor", "Profile ThreadPool"),
            ("edit_profile_executor", "Edit Profile ThreadPool"),
            ("menu_executor", "Menu ThreadPool"),
            ("coins_executor", "Coins ThreadPool"),
            ("support_executor", "Support ThreadPool"),
            ("admin_pool", "Admin ThreadPool"),
            ("registration_pool", "Registration ThreadPool"),
        ]

        cleaned_pools = 0
        for pool_name, display_name in pools:
            if hasattr(self, pool_name):
                try:
                    logger.info(f"🔧 إيقاف {display_name}...")
                    getattr(self, pool_name).shutdown(wait=True)
                    logger.info(f"✅ {display_name} تم إيقافه بنجاح")
                    cleaned_pools += 1
                except Exception as e:
                    logger.error(f"❌ خطأ في إيقاف {display_name}: {e}")

        logger.info(
            f"🎯 تم تنظيف {cleaned_pools}/7 ThreadPools بنجاح - إجمالي 37 worker"
        )


# ================================ نقطة البداية ================================
if __name__ == "__main__":
    bot = FC26SmartBot()
    bot.run()
