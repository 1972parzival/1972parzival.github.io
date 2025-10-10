import type { Metadata } from "next";
import { Jost } from "next/font/google";
import "./globals.css";
import Layout from "@/components/Layout";

const jost = Jost({
  subsets: ["latin"],
  weight: ["100", "200", "300", "400", "500", "600", "700", "800", "900"],
  style: ["normal", "italic"],
});

export const metadata: Metadata = {
  title: "Archie Haddley-Morris ",
  description: "This is my website for showcasing some of the projects I work on and services I provide.",
  keywords: "",
  authors: [{ name: "Archie Haddley-Morris" }],
  creator: "Archie Haddley-Morris",
  openGraph: {
    type: "website",
    locale: "en_US",
    url: "https://parz.wiki",
    title: "Archie Haddley-Morris ",
    description: "This is my website for showcasing some of the projects I work on and services I provide.",
    siteName: "Archie Haddley-Morris ",
  },
  twitter: {
    card: "summary_large_image",
    title: "Archie Haddley-Morris ",
    description: "This is my website for showcasing some of the projects I work on and services I provide.",
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="en">
      <head>
        {/* eslint-disable @next/next/no-css-tags */}
        {/* Original Mobirise CSS files */}
        <link rel="stylesheet" href="/assets/web/assets/mobirise-icons/mobirise-icons.css" />
        <link rel="stylesheet" href="/assets/web/assets/mobirise-icons2/mobirise2.css" />
        <link rel="stylesheet" href="/assets/web/assets/mobirise-icons-bold/mobirise-icons-bold.css" />
        <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap.min.css" />
        <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap-grid.min.css" />
        <link rel="stylesheet" href="/assets/bootstrap/css/bootstrap-reboot.min.css" />
        <link rel="stylesheet" href="/assets/dropdown/css/style.css" />
        <link rel="stylesheet" href="/assets/socicon/css/styles.css" />
        <link rel="stylesheet" href="/assets/theme/css/style.css" />
        <link rel="stylesheet" href="/assets/mobirise/css/mbr-additional.css" />
        <link rel="stylesheet" href="/prism.css" />
        {/* eslint-enable @next/next/no-css-tags */}
      </head>
      <body className={`${jost.className} antialiased`}>
        <Layout>{children}</Layout>
      </body>
    </html>
  );
}