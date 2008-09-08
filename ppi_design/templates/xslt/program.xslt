<?xml version="1.0"?>
<xsl:stylesheet id="program" version="1.0" xmlns:xsl="http://www.w3.org/1999/XSL/Transform">
	<xsl:template match="program">
			<xsl:apply-templates/>
	</xsl:template>

	<xsl:template match="section">
		<div class="section"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="subsection">
		<div class="subsection"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="generic">
		<div class="generic"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="list">
		<div class="list">
			<xsl:apply-templates/>
		</div>
	</xsl:template>

	<xsl:template match="list/engine">
		<div class="engine"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="list/address">
		<div class="address"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="list/person">
		<div class="person"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="list/item">
		<div class="item"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="list/numbers">
		<div class="numbers"><xsl:apply-templates/></div>
	</xsl:template>

	<xsl:template match="inline">
		<div class="inline">
			<xsl:apply-templates/>
		</div>
	</xsl:template>

	<xsl:template match="mail">
		<xsl:variable name="mail-address"><xsl:value-of select="@addr"/></xsl:variable>
		<a class="mail" href="mailto:{$mail-address}"><xsl:value-of select="@addr"/></a>
	</xsl:template>

	<xsl:template match="url">
		<xsl:variable name="url-address"><xsl:value-of select="@addr"/></xsl:variable>
		<a class="url" href="http://{$url-address}"><xsl:value-of select="@addr"/></a>
	</xsl:template>

	<xsl:template match="inline//label">
		<div class="label"><xsl:appy-templates/></div>
	</xsl:template>

	<xsl:template match="inline//data">
		<div class="data"><xsl:apply-templates /></div>
	</xsl:template>


</xsl:stylesheet>
