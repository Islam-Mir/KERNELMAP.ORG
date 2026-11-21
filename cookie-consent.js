/*
 * Google AdSense + Google Analytics 4
 * Google Privacy & Messaging
 * Basic Consent Mode
 * KernelMap.org
 */

(function () {
  "use strict";

  const ADSENSE_CLIENT = "ca-pub-4240610713346131";
  const GA4_ID = "G-GW3S1CKY7Q";

  // =====================================
  // GOOGLE PRIVACY & MESSAGING
  // =====================================

  window.googlefc = window.googlefc || {};
  window.googlefc.callbackQueue = window.googlefc.callbackQueue || [];

  // =====================================
  // GOOGLE ANALYTICS 4
  // =====================================

  function loadGoogleAnalytics() {
    if (window.kernelMapGA4Loaded) {
      return;
    }

    window.kernelMapGA4Loaded = true;

    window.dataLayer = window.dataLayer || [];

    window.gtag =
      window.gtag ||
      function () {
        window.dataLayer.push(arguments);
      };

    window.gtag("js", new Date());
    window.gtag("config", GA4_ID);

    if (
      !document.querySelector('script[src*="googletagmanager.com/gtag/js"]')
    ) {
      const analyticsScript = document.createElement("script");

      analyticsScript.async = true;
      analyticsScript.src =
        "https://www.googletagmanager.com/gtag/js?id=" + GA4_ID;

      document.head.appendChild(analyticsScript);
    }
  }

  // =====================================
  // BASIC CONSENT MODE
  // =====================================

  window.googlefc.callbackQueue.push({
    CONSENT_MODE_DATA_READY: function () {
      try {
        const consentValues = window.googlefc.getGoogleConsentModeValues();

        const consentEnum = window.googlefc.ConsentModePurposeStatusEnum;

        if (!consentValues || !consentEnum) {
          return;
        }

        const analyticsStatus =
          consentValues.analyticsStoragePurposeConsentStatus;

        const analyticsGranted =
          analyticsStatus === consentEnum.GRANTED ||
          analyticsStatus === consentEnum.NOT_APPLICABLE;

        if (analyticsGranted) {
          loadGoogleAnalytics();
        }
      } catch (error) {
        console.error(
          "KernelMap: errore nella verifica del consenso Analytics.",
          error,
        );
      }
    },
  });

  // =====================================
  // GOOGLE ADSENSE
  // =====================================

  window.adsbygoogle = window.adsbygoogle || [];

  if (
    !document.querySelector(
      'script[src*="pagead2.googlesyndication.com/pagead/js/adsbygoogle.js"]',
    )
  ) {
    const adsenseScript = document.createElement("script");

    adsenseScript.async = true;
    adsenseScript.src =
      "https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=" +
      ADSENSE_CLIENT;

    adsenseScript.crossOrigin = "anonymous";

    document.head.appendChild(adsenseScript);
  }
})();
