<?xml version="1.0"?>
<xsl:stylesheet id="toprogram" version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">

    <xsl:template match="lang">
        <lang><xsl:apply-templates /></lang>
    </xsl:template>

    <xsl:template match="program">
        <program>
            <xsl:apply-templates/>
        </program>
    </xsl:template>

    <xsl:template match="div[@class='section']">
        <section><xsl:apply-templates /></section>
    </xsl:template>

    <xsl:template match="div[@class='subsection']">
        <subsection><xsl:apply-templates /></subsection>
    </xsl:template>

    <xsl:template match="div[@class='generic']">
        <generic><xsl:apply-templates /></generic>
    </xsl:template>

    <xsl:template match="div[@class='list']">
        <list><xsl:apply-templates /></list>
    </xsl:template>

    <xsl:template match="div[@class='list']/div[@class='engine']">
        <engine><xsl:apply-templates /></engine>
    </xsl:template>

    <xsl:template match="div[@class='list']/div[@class='engine']">
        <item><xsl:apply-templates /></item>
    </xsl:template>

    <xsl:template match="div[@class='list']/div[@class='address']">
        <address><xsl:apply-templates /></address>
    </xsl:template>

    <xsl:template match="div[@class='list']/div[@class='person']">
        <person><xsl:apply-templates /></person>
    </xsl:template>

    <xsl:template match="div[@class='list']/div[@class='item']">
        <item><xsl:apply-templates /></item>
    </xsl:template>

    <xsl:template match="div[@class='list']/div[@class='numbers']">
        <numbers><xsl:apply-templates /></numbers>
    </xsl:template>

    <xsl:template match="div[@class='inline']">
        <inline><xsl:apply-templates /></inline>
    </xsl:template>

    <xsl:template match="a[@class='mail']">
        <xsl:variable name="mail-address"><xsl:value-of select="@href"/></xsl:variable>
        <mail addr='{$mail-address}' />
    </xsl:template>

    <xsl:template match="a[@class='url']">
        <xsl:variable name="mail-address"><xsl:value-of select="@href"/></xsl:variable>
        <url addr='{$mail-address}' />
    </xsl:template>

    <xsl:template match="url">
        <xsl:variable name="url-address"><xsl:value-of select="@addr"/></xsl:variable>
        <a href="http://{$url-address}"><xsl:value-of select="@addr"/></a>
    </xsl:template>

    <xsl:template match="div[@class='inline']/div[@class='label']">
        <label><xsl:apply-templates /></label>
    </xsl:template>

    <xsl:template match="div[@class='inline']/div[@class='data']">
        <data><xsl:apply-templates /></data>
    </xsl:template>

</xsl:stylesheet>
