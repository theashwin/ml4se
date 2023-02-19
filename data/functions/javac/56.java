protected ResponseEntity<String> createResponseEntityForTicket(final HttpServletRequest request,
                                                                   final TicketGrantingTicket tgtId) throws Exception {
        return this.ticketGrantingTicketResourceEntityResponseFactory.build(tgtId, request);
    }